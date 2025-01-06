# GoLaundry MQTT Client

## Deskripsi Program
GoLaundry MQTT Client adalah sebuah aplikasi berbasis Python yang memanfaatkan protokol MQTT untuk komunikasi pesan. Program ini dirancang untuk mensimulasikan komunikasi antara pengguna dengan layanan laundry menggunakan topik MQTT. Program ini dibuat untuk memenuhi tugas mata kuliah **Sistem Informasi** oleh **Faqihuddin Habibi**.

## Fitur
- Memilih layanan laundry berdasarkan lokasi:
  - Laundry Bojong (1 Hari)
  - Laundry Soang (3 Hari)
- Mengirim pesan ke topik MQTT tertentu.
- Menampilkan pesan yang diterima dari topik yang dipilih.
- Mendukung koneksi multi-klien.
- Fitur pemberitahuan ketika pengguna bergabung atau meninggalkan topik.

## Persyaratan Sistem
1. Python 3.7 atau versi yang lebih baru.
2. Modul Python berikut:
   - `paho-mqtt`
3. Broker MQTT yang aktif pada alamat dan port yang ditentukan dalam kode (default: `localhost:3333`).

## Instalasi
1. Clone repository ini:
   ```bash
   git clone https://github.com/fhabibiii/GoLaundry.git
   cd GoLaundry
   ```
2. Install dependensi yang dibutuhkan:
   ```bash
   pip install paho-mqtt
   ```

## Cara Penggunaan
1. Jalankan broker MQTT (misalnya, Mosquitto) di perangkat lokal atau server.
2. Eksekusi program:
   ```bash
   python3 GoLaundry.py
   ```
3. Masukkan nama pengguna (username) untuk bergabung dalam sesi komunikasi.
4. Pilih layanan laundry:
   - Ketik `1` untuk Laundry Bojong (1 Hari).
   - Ketik `2` untuk Laundry Soang (3 Hari).
   - Ketik `0` untuk keluar dari program.
5. Ketik pesan Anda dan tekan Enter untuk mengirim.
6. Ketik `exit` untuk keluar dari topik.

## Struktur Program
- **`connect`**: Menghubungkan klien ke broker MQTT.
- **`publish`**: Mengirim pesan ke topik tertentu.
- **`subscribe`**: Mendengarkan pesan yang diterima pada topik.
- **`run`**: Fungsi utama yang menjalankan logika program.

## Catatan Tambahan
- Pastikan broker MQTT berjalan dengan baik sebelum menjalankan program.
- Jika menggunakan broker di perangkat lain, sesuaikan alamat `broker_address` pada kode.
- Sesuaikan port dan topik sesuai kebutuhan.

## Kontributor
- Nama: Faqihuddin Habibi
- Mata Kuliah: Sistem Informasi

## Lisensi
Program ini dilisensikan di bawah [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html). Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan ulang program ini selama mengikuti ketentuan lisensi.

---
Dibuat dengan ❤ oleh **Faqihuddin Habibi** 🍉
