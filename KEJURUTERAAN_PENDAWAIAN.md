# Seni Bina Pendawaian & Tetapan Cip STN — StealthX Universal

## 1. Susunan Pin Standard Port Diagnostik OBD-II (SAE J1962 16-Pin)
- **Pin 4:** Bumi Casis (*Chassis Ground*)
- **Pin 5:** Bumi Isyarat (*Signal Ground*)
- **Pin 6:** `CAN-High` (`ISO 15765-4`, `500 kbps`)
- **Pin 14:** `CAN-Low` (`ISO 15765-4`, `500 kbps`)
- **Pin 16:** Bekalan Kuasa Tetap Bateri (`+12V DC`)

## 2. Tetapan Wajib Penyesuai Cip STN
- **Protokol Pilihan:** `ISO 15765-4 CAN (11-bit ID, 500 kbps)`
- **Mod Komunikasi Pantas (*STN Fast Mode*):** Diaktifkan (`ON`)
- **Mod Jimat Bateri (*Auto Sleep*):** Diaktifkan (`ON`, arus tidur `< 2 mA`)
- **Keutamaan Tinggi (`100–200 ms`):** `RPM (010C)`, `Load (0104)`, `TPS (0111)`, `MAF (0110)`.
- **Keutamaan Rendah (`1,000–2,000 ms`):** `ECT (0105)`, `IAT (010F)`, `Suhu Transmisi`, `LTFT (0107)`, `Voltan (0142)`.

## 3. Rujukan Pengepala ECU (*Header*)
- **ECU Enjin (*ECM*):** `7E0` (Jawapan: `7E8`)
- **ECU Transmisi (*TCM*):** `7E1` (Jawapan: `7E9`) atau `7E2` (Jawapan: `7EA`)
