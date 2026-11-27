#!/usr/bin/env python3
"""StealthX Universal — Penasihat Kecekapan & Diagnosis Kesihatan Enjin Masa Nyata"""

import time

try:
    import serial
except ImportError:
    serial = None

PORT_BERSIRI = "/dev/rfcomm0"
KADAR_BAUD = 115200


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


def nilai_status(rpm: float, beban: float, tps: float, ect: int, ltft: float, volt: float) -> str:
    amaran = []
    if ect >= 98:
        amaran.append(f"[KRITIKAL TERMA] Suhu Enjin Tinggi ({ect}C) - Periksa Kipas/Radiator!")
    if volt > 0 and volt < 12.2:
        amaran.append(f"[ELEKTRIKAL] Voltan Rendah ({volt}V) - Semak Alternator/Bateri!")
    if abs(ltft) > 10.0:
        arah = "Terlalu Nipis (Lean/Vakum Bocor)" if ltft > 0 else "Terlalu Kaya (Rich/Penapis Udara Kotor)"
        amaran.append(f"[CAMPURAN API] LTFT {ltft:+.1f}% ({arah})")
    if amaran:
        return " | ".join(amaran)
    if 1450 <= rpm <= 2050 and 20.0 <= beban <= 45.0 and tps <= 25.0:
        return "[ZON HIJAU STEALTHX] Kecekapan Bahan Api Optimum & Enjin Dingin"
    if rpm > 2300 or tps > 32.0:
        return "[NASIHAT PENDIKIT] Ringankan pedal untuk kembali ke zon 1,500-2,000 RPM"
    return "[OPERASI NORMAL] Roh OEM Terpelihara"


def jalankan_penasihat():
    if serial is None:
        print("Ralat: Sila jalankan 'pip install pyserial' terlebih dahulu.")
        return

    with serial.Serial(PORT_BERSIRI, KADAR_BAUD, timeout=1) as obd:
        for c in ("ATZ", "ATE0", "ATL0", "ATS0", "ATSP6"):
            hantar(obd, c)
        print("=== STEALTHX UNIVERSAL ECO & HEALTH ADVISOR AKTIF ===")
        try:
            while True:
                r = bait(hantar(obd, "010C"), "410C")
                l = bait(hantar(obd, "0104"), "4104")
                t = bait(hantar(obd, "0111"), "4111")
                e = bait(hantar(obd, "0105"), "4105")
                f = bait(hantar(obd, "0107"), "4107")
                v = bait(hantar(obd, "0142"), "4142")

                rpm = round(((r[0] * 256) + r[1]) / 4, 0) if len(r) >= 2 else 0
                beban = round((l[0] * 100) / 255, 1) if l else 0.0
                tps = round((t[0] * 100) / 255, 1) if t else 0.0
                ect = (e[0] - 40) if e else 0
                ltft = round((f[0] - 128) * 100 / 128, 1) if f else 0.0
                volt = round(((v[0] * 256) + v[1]) / 1000, 2) if len(v) >= 2 else 0.0

                status = nilai_status(rpm, beban, tps, ect, ltft, volt)
                print(f"RPM:{rpm:4.0f} | Beban:{beban:4.1f}% | TPS:{tps:4.1f}% | ECT:{ect:2d}C | LTFT:{ltft:+5.1f}% | {volt:4.2f}V >> {status}")
                time.sleep(0.6)
        except KeyboardInterrupt:
            print("\nPenasihat StealthX ditamatkan.")


if __name__ == "__main__":
    jalankan_penasihat()
