# GoLaundry: Sistem Informasi Pemantauan Laundry Berbasis MQTT

GoLaundry adalah aplikasi berbasis Python yang menggunakan protokol MQTT untuk mengelola dan memantau aktivitas laundry di berbagai lokasi. Program ini dikembangkan untuk memenuhi Tugas Besar Sistem Informasi.

## Fitur Utama
1. **Publikasi dan Langganan MQTT**: Menggunakan protokol MQTT untuk komunikasi antar-klien.
2. **Pilihan Lokasi Laundry**:
   - Laundry Bojong (1 Hari)
   - Laundry Soang (3 Hari)
3. **Sistem Notifikasi**:
   - Notifikasi saat pengguna bergabung atau keluar dari layanan.
   - Pesan antar pengguna dalam sistem yang sama.
4. **Multi-threading**: Memastikan aplikasi tetap responsif dengan memisahkan proses komunikasi dan UI.

## Persyaratan Sistem
- Python 3.6 atau lebih baru
- Paket Python:
  - `paho-mqtt`
  - `threading`
  - `random`
- Server MQTT yang dapat dijalankan di localhost
