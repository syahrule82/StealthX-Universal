#!/usr/bin/env python3
"""StealthX Universal — Perakam Telemetri & Kecekapan Bahan Api (OBD-II Mode 01)"""

import csv
import os
import time
from datetime import datetime

try:
    import serial
except ImportError:
    serial = None

PORT_BERSIRI = "/dev/rfcomm0"
KADAR_BAUD = 115200
DIREKTORI_LOG = "log_perjalanan"
JENIS_BAHAN_API = "PETROL"  # Tukar kepada "DIESEL" jika perlu


def hantar(obd, cmd: str) -> str:
    obd.write((cmd + "\r").encode("ascii"))
    time.sleep(0.08)
    raw = obd.read(obd.in_waiting or 64).decode("ascii", errors="ignore")
    baris = [b.strip() for b in raw.splitlines() if b.strip() and ">" not in b]
    return baris[-1].replace(" ", "") if baris else ""


def bait(heks: str, awalan: str) -> list[int]:
    if not heks.startswith(awalan):
        return []
    isi = heks[len(awalan):]
    return [int(isi[i:i + 2], 16) for i in range(0, len(isi), 2) if len(isi[i:i + 2]) == 2]


def jalankan():
    if serial is None:
        print("Ralat: Pasang pustaka dahulu -> pip install pyserial")
        return

    afr, ketumpatan = (14.5, 835.0) if JENIS_BAHAN_API.upper() == "DIESEL" else (14.7, 745.0)
    os.makedirs(DIREKTORI_LOG, exist_ok=True)
    fail_log = os.path.join(DIREKTORI_LOG, f"stealthx_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

    with serial.Serial(PORT_BERSIRI, KADAR_BAUD, timeout=1) as obd, open(fail_log, "w", newline="", encoding="utf-8") as f:
        for c in ("ATZ", "ATE0", "ATL0", "ATS0", "ATSP6"):
            hantar(obd, c)
        w = csv.writer(f)
        w.writerow(["Masa", "RPM", "Kelajuan_kmj", "Beban_%", "Pendikit_%", "IAT_C", "ECT_C", "MAF_gs", "Anggaran_kmL", "Voltan_V"])
        print(f"Merekod ke {fail_log} (Tekan Ctrl+C untuk berhenti)")
        try:
            while True:
                r = bait(hantar(obd, "010C"), "410C")
                s = bait(hantar(obd, "010D"), "410D")
                l = bait(hantar(obd, "0104"), "4104")
                t = bait(hantar(obd, "0111"), "4111")
                i = bait(hantar(obd, "010F"), "410F")
                e = bait(hantar(obd, "0105"), "4105")
                m = bait(hantar(obd, "0110"), "4110")
                v = bait(hantar(obd, "0142"), "4142")

                rpm = round(((r[0] * 256) + r[1]) / 4, 1) if len(r) >= 2 else 0.0
                spd = s[0] if s else 0
                lod = round((l[0] * 100) / 255, 1) if l else 0.0
                tps = round((t[0] * 100) / 255, 1) if t else 0.0
                iat = (i[0] - 40) if i else 0
                ect = (e[0] - 40) if e else 0
                maf = round(((m[0] * 256) + m[1]) / 100, 2) if len(m) >= 2 else 0.0
                vlt = round(((v[0] * 256) + v[1]) / 1000, 2) if len(v) >= 2 else 0.0
                lj = (maf * 3600) / (afr * ketumpatan) if maf > 0 else 0.0
                kml = round(spd / lj, 2) if lj > 0 and spd > 0 else 0.0

                w.writerow([datetime.now().strftime("%H:%M:%S"), rpm, spd, lod, tps, iat, ect, maf, kml, vlt])
                f.flush()
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nSesi perekodan ditamatkan dengan selamat.")


if __name__ == "__main__":
    jalankan()
