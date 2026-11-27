# StealthX Automotive Telemetry — Kerangka Pemantauan & Kecekapan Kenderaan Universal

Kerangka kejuruteraan sumber terbuka untuk menukar telefon pintar Android menjadi panel telemetri masa nyata, penasihat pemanduan cekap bahan api (*eco-cruise*), dan sistem amaran awal kesihatan terma tanpa mengubah suai perisian ECU asal kilang.

## 1. Falsafah Kejuruteraan: "Roh OEM Terpelihara" (*Zero-Footprint*)
Suntikan optimasi **StealthX** beroperasi secara **bacaan sahaja (*non-invasive read-only*)** melalui rangkaian diagnostik **OBD-II (ISO 15765-4 CAN)**:
- **Integriti ECU Kilang 100% Utuh:** Tidak melibatkan pemetaan semula ECU atau pemotongan pendawaian asal. Segala perlindungan keselamatan kilang kekal beroperasi sepenuhnya.
- **Pencegahan Awal (*Predictive Monitoring*):** Menggantikan tolok penampan papan pemuka kilang dengan bacaan sensor sebenar bagi mengesan kenaikan suhu penyejuk enjin dan bendalir transmisi lebih awal.
- **Sifar Kesan Kekal:** Apabila penyesuai OBD-II dicabut daripada port 16-pin, kenderaan kembali kepada keadaan asal kilang sepenuhnya.

## 2. Seni Bina Modular Dua Peringkat
1. **Peringkat 1 — Teras Telemetri & Kecekapan Perisian (Wajib Ada Penyesuai OBD-II):** Penyesuai cip **STN** (*Vgate vLinker MC+*, *Vgate vLinker FS*, atau *OBDLink MX+*) dengan mod tidur automatik (`< 2 mA`), digabungkan dengan aplikasi **Torque Pro** / **RealDash** serta **Termux**.
2. **Peringkat 2 — Modifikasi Fizikal StealthX (Pilihan Lanjutan):** Penebatan haba ruang enjin, penstabilan voltan bebas hingar (`EMI`), dan pembumian bintang (*Star Ground*).

## 3. Penentukuran Zon Hijau Papan Pemuka (*StealthX 2-Page UI*)
| Halaman Paparan | Parameter Utama | Kereta Aspirasi Biasa (NA + CVT/AT) | Kereta Turbo (TGDI + DCT) |
| :--- | :--- | :--- | :--- |
| **Halaman 1: Eco-Cruise** | **Putaran Enjin (`RPM`)** | `1,500 – 2,000 RPM` *(Amaran > 2,200)* | `1,600 – 2,200 RPM` |
| **Halaman 1: Eco-Cruise** | **Beban Enjin (`Load`)** | `25% – 45%` | `20% – 40%` |
| **Halaman 1: Eco-Cruise** | **Bukaan Pendikit (`TPS`)** | `16% – 24%` | `14% – 22%` |
| **Halaman 2: Terma** | **Suhu Udara Masuk (`IAT`)** | `< 45 °C` semasa bergerak | `< 50 °C` |
| **Halaman 2: Terma** | **Suhu Penyejuk (`ECT`)** | `82 °C – 93 °C` | `85 °C – 98 °C` |
| **Halaman 2: Terma** | **Suhu Bendalir Transmisi** | `65 °C – 85 °C` *(Amaran bunyi 98 °C)* | `70 °C – 90 °C` *(Amaran 105 °C)* |
| **Halaman 2: Elektrikal** | **Voltan Sistem (`12V`)** | `12.4V – 14.4V` | `12.6V – 14.8V` |
