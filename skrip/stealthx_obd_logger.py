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


def hantar_perintah(sambungan, perintah: str) -> str:
    sambungan.write((perintah + "\r").encode("ascii"))
    time.sleep(0.08)
    data = sambungan.read(sambungan.in_waiting or 64).decode("ascii", errors="ignore")
    baris = [b.strip() for b in data.splitlines() if b.strip() and ">" not in b]
    return baris[-1].replace(" ", "") if baris else ""


def nyahkod(heks: str, awalan: str) -> list[int]:
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
        for cmd in ("ATZ", "ATE0", "ATL0", "ATS0", "ATSP6"):
            hantar_perintah(obd, cmd)

        penulis = csv.writer(f)
        penulis.writerow(["Masa", "RPM", "Kelajuan_kmj", "Beban_%", "Pendikit_%", "IAT_C", "ECT_C", "MAF_gs", "Anggaran_kmL", "Voltan_V"])
        print(f"Merekod telemetri ke {fail_log} (Tekan Ctrl+C untuk berhenti)")

        try:
            while True:
                rpm_b = nyahkod(hantar_perintah(obd, "010C"), "410C")
                spd_b = nyahkod(hantar_perintah(obd, "010D"), "410D")
                lod_b = nyahkod(hantar_perintah(obd, "0104"), "4104")
                thr_b = nyahkod(hantar_perintah(obd, "0111"), "4111")
                iat_b = nyahkod(hantar_perintah(obd, "010F"), "410F")
                ect_b = nyahkod(hantar_perintah(obd, "0105"), "4105")
                maf_b = nyahkod(hantar_perintah(obd, "0110"), "4110")
                vlt_b = nyahkod(hantar_perintah(obd, "0142"), "4142")

                rpm = round(((rpm_b[0] * 256) + rpm_b[1]) / 4, 1) if len(rpm_b) >= 2 else 0.0
                kelajuan = spd_b[0] if spd_b else 0
                beban = round((lod_b[0] * 100) / 255, 1) if lod_b else 0.0
                pendikit = round((thr_b[0] * 100) / 255, 1) if thr_b else 0.0
                iat = (iat_b[0] - 40) if iat_b else 0
                ect = (ect_b[0] - 40) if ect_b else 0
                maf = round(((maf_b[0] * 256) + maf_b[1]) / 100, 2) if len(maf_b) >= 2 else 0.0
                voltan = round(((vlt_b[0] * 256) + vlt_b[1]) / 1000, 2) if len(vlt_b) >= 2 else 0.0

                liter_jam = (maf * 3600) / (afr * ketumpatan) if maf > 0 else 0.0
                km_liter = round(kelajuan / liter_jam, 2) if liter_jam > 0 and kelajuan > 0 else 0.0

                penulis.writerow([datetime.now().strftime("%H:%M:%S"), rpm, kelajuan, beban, pendikit, iat, ect, maf, km_liter, voltan])
                f.flush()
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nSesi perekodan ditamatkan dengan selamat.")


if __name__ == "__main__":
    jalankan()
