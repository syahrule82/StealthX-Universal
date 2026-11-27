# StealthX Automotive Telemetry — Kerangka Pemantauan & Kecekapan Kenderaan Universal

Kerangka kejuruteraan sumber terbuka untuk menukar telefon pintar Android menjadi panel telemetri masa nyata, penasihat pemanduan cekap bahan api (*eco-cruise*), dan sistem amaran awal kesihatan terma tanpa mengubah suai perisian ECU asal kilang.

## 1. Falsafah Kejuruteraan: "Roh OEM Terpelihara" (*Zero-Footprint*)
- **Integriti ECU Kilang 100% Utuh:** Beroperasi secara bacaan sahaja (*non-invasive read-only*) melalui OBD-II (`ISO 15765-4 CAN`) tanpa pemetaan semula ECU atau pemotongan wayar.
- **Pencegahan Awal (*Predictive Monitoring*):** Menggantikan tolok penampan kilang dengan bacaan sensor sebenar bagi mengesan kenaikan suhu enjin dan transmisi lebih awal.
- **Sifar Kesan Kekal:** Kenderaan kembali ke keadaan kilang 100% sebaik sahaja penyesuai OBD-II dicabut.

## 2. Seni Bina Modular Dua Peringkat
1. **Peringkat 1 — Teras Telemetri Perisian (Wajib Ada Penyesuai OBD-II):** Penyesuai cip **STN** (*Vgate vLinker MC+*, *vLinker FS*, atau *OBDLink MX+*) dengan mod tidur automatik (`< 2 mA`), bersama **Torque Pro** / **RealDash** dan **Termux**.
2. **Peringkat 2 — Modifikasi Fizikal StealthX (Pilihan Lanjutan):** Penebatan haba ruang enjin, penstabilan voltan bebas hingar (`EMI`), dan pembumian bintang (*Star Ground*).

## 3. Penentukuran Zon Hijau Papan Pemuka (*StealthX 2-Page UI*)
| Halaman | Parameter | Aspirasi Biasa (NA + CVT/AT) | Turbo (TGDI + DCT) |
| :--- | :--- | :--- | :--- |
| **1: Eco-Cruise** | **Putaran Enjin (`RPM`)** | `1,500 – 2,000 RPM` *(Amaran > 2,200)* | `1,600 – 2,200 RPM` |
| **1: Eco-Cruise** | **Beban Enjin (`Load`)** | `25% – 45%` | `20% – 40%` |
| **1: Eco-Cruise** | **Bukaan Pendikit (`TPS`)** | `16% – 24%` | `14% – 22%` |
| **2: Terma** | **Suhu Udara Masuk (`IAT`)** | `< 45 °C` semasa bergerak | `< 50 °C` |
| **2: Terma** | **Suhu Penyejuk (`ECT`)** | `82 °C – 93 °C` | `85 °C – 98 °C` |
| **2: Terma** | **Suhu Transmisi** | `65 °C – 85 °C` *(Amaran 98 °C)* | `70 °C – 90 °C` *(Amaran 105 °C)* |
| **2: Elektrikal** | **Voltan Sistem (`12V`)** | `12.4V – 14.4V` | `12.6V – 14.8V` |

## 4. Kandungan Fail Tambahan Komuniti
- **`RUJUKAN_PID_MALAYSIA.md`:** Jadual kod PID suhu bendalir transmisi (`CVT / D-CVT / AT / 7DCT`) bagi Perodua, Toyota, Honda, Proton, Mazda, Nissan, dan Mitsubishi.
- **`skrip/stealthx_eco_advisor.py`:** Penasihat masa nyata di terminal yang mengesan zon *eco-cruise*, kebocoran vakum melalui `LTFT`, kesihatan alternator, dan amaran awal suhu enjin.
