# UASDjangoSocialNetwork

## Deskripsi Proyek
UASDjangoSocialNetwork adalah proyek aplikasi jejaring sosial yang dibangun dengan Django, menyediakan fitur seperti registrasi akun, pertemanan, obrolan waktu nyata, notifikasi, dan umpan berita. Proyek ini bertujuan untuk menyediakan platform sosial dasar dengan fitur interaksi pengguna yang sederhana dan fungsional.

## Sumber Referensi
- [Gatherly - Pdshetley](https://github.com/pdshetley/Gatherly)

## Daftar Pekerjaan

### Akun (Accounts)
1. Membuat Model (Selesai)
2. Membuat Views untuk halaman Registrasi dan Login (Selesai)
3. Routing URL (Selesai)
4. Pengujian

### Fungsi Sosial
1. Abstraksi model untuk Obrolan
2. Abstraksi views untuk pesan antar teman
3. Menambahkan fungsi untuk obrolan waktu nyata menggunakan pola desain perintah
4. Routing websocket untuk Obrolan
5. Pengujian

### Middleware Login
1. Fungsi Home untuk mengarahkan ke halaman login jika pengguna belum login
2. Menambahkan URL
3. Pengujian

### Model Teman (Friends)
1. Abstraksi model untuk Model Teman
2. Pola desain perintah untuk fungsi terkait
3. Views
4. URL
5. Routing notifikasi waktu nyata untuk permintaan pertemanan
6. Pengujian

### Media
1. Penampungan untuk foto profil
2. Pengujian

### Newsfeed
1. Abstraksi model untuk Post dan Komentar
2. Views
3. URL
4. Pengujian

### Notifikasi
1. Model untuk Notifikasi?
2. Fungsi Pola Perintah Notifikasi
3. Routing notifikasi waktu nyata
4. Views
5. URL
6. Pengujian

### Profil Pengguna (UserProfile)
1. Abstraksi Model
2. Views
3. URL

### Frontend
1. Halaman Login
2. Halaman Registrasi
3. Halaman Beranda
4. Template HTML dasar
5. Pesan
6. Temukan Teman
7. Sidebar Statis

### Utama (Main)
1. Pengaturan `settings.py`
2. Pengaturan Routing
3. Pengaturan URL
4. Pengaturan Websocket

## Dokumentasi

### Akun (Accounts)
1. User Model: Model pengguna yang diperluas dengan menambahkan atribut khusus seperti gender, status, dan about.
2. RegisterView: Tampilan untuk halaman registrasi yang menciptakan pengguna baru.
3. LoginView: Tampilan untuk halaman login yang mengautentikasi pengguna berdasarkan email dan password.
4. LogoutView: Fungsi logout yang mengeluarkan pengguna dari akun mereka.
5. UserRegistrationForm: Formulir pendaftaran untuk pengguna baru dengan validasi tambahan, termasuk pengecekan nama pengguna.
6. UserLoginForm: Formulir login untuk pengguna, dengan validasi email dan password.