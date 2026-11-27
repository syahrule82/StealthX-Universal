# Rujukan Silang PID Transmisi & Enjin Kereta Malaysia — StealthX Universal

Gantikan baris `StealthX Transmission Temp (Templat)` di dalam fail `telemetri/StealthX_Universal_PID.csv` mengikut jenama kenderaan anda di bawah. Semua parameter menggunakan mod bacaan pasif (`read-only`) tanpa mengubah tetapan ECU kilang.

## 1. Perodua & Toyota / Daihatsu (Myvi, Alza, Bezza, Axia, Ativa, Vios, Yaris)
* **Jenis Transmisi:** `E-AT 4-Kelajuan` & `D-CVT`
* **Protokol:** `ISO 15765-4 CAN (11-bit, 500 kbps)`
* **Konfigurasi Baris CSV Torque Pro:**
  * **Suhu Bendalir Transmisi (`ATF / D-CVT`):** `ModeAndPID`: `2182` | `Equation`: `((((A*256)+B)*7/100)-400)/10` | `Header`: `7E0` (atau `7E1` bagi model D-CVT baharu)
  * **Alternatif Suhu Transmisi (`Mode 21 D9`):** `ModeAndPID`: `21D9` | `Equation`: `((((G*256)+H)*7/100)-400)/10` | `Header`: `7E0`
* **Julat Operasi Sihat:** `65 °C – 88 °C` *(Tetapkan amaran bunyi pada `100 °C`)*

## 2. Honda (City GM6/GN2, Jazz GK5, Civic FC/FE, HR-V, BR-V, CR-V)
* **Jenis Transmisi:** `Earth Dreams CVT` (`Honda HCF-2`)
* **Konfigurasi Baris CSV Torque Pro:**
  * **Suhu Bendalir CVT:** `ModeAndPID`: `222201` | `Equation`: `A-40` *(atau `((A*256)+B)/100` bagi generasi turbo)* | `Header`: `7E1`
  * **Dwi-Suhu Penyejuk (`ECT 1` & `ECT 2`):** `ModeAndPID`: `0167` | `Equation ECT 1`: `B-40` | `Equation ECT 2`: `C-40` | `Header`: `7E0`
* **Julat Operasi Sihat:** `65 °C – 85 °C` *(Tetapkan amaran bunyi pada `98 °C`)*

## 3. Proton & Geely (Saga VVT, Persona, Iriz, X50, X70, S70)
* **Jenis Transmisi:** `Punch CVT`, `4AT`, & `7-Speed Dual Clutch (7DCT)`
* **Konfigurasi Baris CSV Torque Pro:**
  * **Suhu Transmisi (`7DCT / Punch CVT`):** `ModeAndPID`: `221940` *(atau `222201`)* | `Equation`: `A-40` | `Header`: `7E1` (atau `7E2`)
  * **Suhu Minyak Enjin (`Engine Oil Temp`):** `ModeAndPID`: `015C` | `Equation`: `A-40` | `Header`: `7E0`
* **Julat Operasi Sihat:** `70 °C – 92 °C` *(Amaran bunyi pada `105 °C` untuk `7DCT` dan `98 °C` untuk `CVT`)*

## 4. Mazda (Mazda2, Mazda3, CX-3, CX-5 — Skyactiv-G / Skyactiv-D)
* **Jenis Transmisi:** `Skyactiv-Drive 6AT`
* **Konfigurasi Baris CSV Torque Pro:**
  * **Suhu Bendalir ATF:** `ModeAndPID`: `221E1C` | `Equation`: `((A*256)+B)/100` | `Header`: `7E1`
* **Julat Operasi Sihat:** `65 °C – 90 °C` *(Amaran bunyi pada `105 °C`)*

## 5. Nissan & Mitsubishi (Almera, X-Trail, Serena, Triton, Xpander)
* **Jenis Transmisi:** `Jatco Xtronic CVT` & `INVECS-III CVT`
* **Konfigurasi Baris CSV Torque Pro:**
  * **Suhu Bendalir CVT:** `ModeAndPID`: `2103` *(Nissan)* atau `2110` *(Mitsubishi)* | `Equation`: `A-40` | `Header`: `7E1`
* **Julat Operasi Sihat:** `60 °C – 85 °C` *(Amaran bunyi pada `95 °C` — transmisi Jatco sangat sensitif terhadap haba)*

## 6. Panduan Mengesan PID Transmisi Jika Tiada Dalam Senarai
1. Pastikan penyesuai **cip STN** (*vLinker MC+ / OBDLink*) berada dalam mod `ISO 15765-4 CAN (500 kbps)`.
2. Di dalam aplikasi **Torque Pro** > **Manage extra PIDs/Sensors**, uji pertanyaan `222201` dan `2182` pada pengepala `7E1` terlebih dahulu dengan enjin hidup pada suhu operasi.
3. Nilai yang sah mesti berada antara **`45 °C` hingga `95 °C`** dan meningkat perlahan-lahan semasa kereta dipandu.
