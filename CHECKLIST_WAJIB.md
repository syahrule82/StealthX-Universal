# Senarai Semak Wajib StealthX Universal

## Fasa 1: Perolehan & Pengesahan Perkakasan
- [ ] Penyesuai OBD-II cip STN tulen (Vgate vLinker MC+ / Vgate vLinker FS / OBDLink MX+).
- [ ] Sahkan fungsi mod tidur automatik (`< 2 mA`) aktif apabila suis pencucuhan dimatikan.
- [ ] Kemas kini perisian tegar (*firmware*) penyesuai melalui aplikasi rasmi pengeluar jika terdapat versi baharu yang sah.

## Fasa 2: Pemasangan Perisian Panel Android
- [ ] Pasang aplikasi **Torque Pro** atau **RealDash** pada telefon pintar panel paparan.
- [ ] Salin fail `telemetri/StealthX_Universal_PID.csv` ke dalam direktori `.torque/extendedpids/`.
- [ ] Import set PID tersuai dan jalankan ujian **Test** pada setiap parameter bagi memastikan tiada ralat `No Data`.
- [ ] Sesuaikan baris `StealthX Transmission Temp` mengikut alamat `Mode 22` atau `Mode 21` model kenderaan anda.

## Fasa 3: Keselamatan Operasi & Pemanduan
- [ ] Tetapkan amaran bunyi (*audible alarm*) bagi suhu penyejuk enjin dan suhu bendalir transmisi.
- [ ] Pastikan pemegang telefon tidak menghalang beg udara (*airbag*) atau pandangan hadapan pemandu.
- [ ] Tanggalkan penyesuai OBD-II sementara waktu sebelum menghantar kenderaan ke pusat servis rasmi.
