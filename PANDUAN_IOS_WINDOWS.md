# Panduan Penggunaan StealthX Universal di iOS & Windows

Kerangka **StealthX Universal** kekal menggunakan protokol bacaan pasif (`OBD-II Mode 01` & `ISO 15765-4 CAN 500 kbps`) tanpa mengubah perisian ECU kilang.

## 1. Pengguna iOS (iPhone / iPad)
- **Syarat Sambungan:** Pastikan penyesuai OBD-II anda menyokong **Bluetooth LE (BLE)** atau **Wi-Fi**. Penyesuai Bluetooth klasik lama yang tidak menyokong BLE/MFi biasanya tidak dapat dipasangkan terus oleh aplikasi iOS.
- **Aplikasi Papan Pemuka:** Gunakan **RealDash** (import `telemetri/stealthx_realdash.xml`) dan rujuk jadual zon hijau serta kod transmisi dalam `RUJUKAN_PID_MALAYSIA.md`.

## 2. Pengguna Windows
- **Sambungan:** Boleh menggunakan **USB**, **Wi-Fi**, atau **Bluetooth Serial (COM Port)**.
- **Menjalankan Skrip Python:** Pasang `pyserial` (`pip install pyserial`), kemudian ubah pemboleh ubah `PORT_BERSIRI = "/dev/rfcomm0"` di dalam `skrip/stealthx_obd_logger.py` atau `skrip/stealthx_eco_advisor.py` kepada port COM Windows anda (contohnya `PORT_BERSIRI = "COM4"`).
