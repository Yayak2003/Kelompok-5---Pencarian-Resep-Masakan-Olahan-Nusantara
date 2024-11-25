# 🍽️ Aplikasi Pencarian Resep Makanan Nusantara

Aplikasi ini adalah platform berbasis **Streamlit** yang memungkinkan pengguna untuk mencari resep makanan Nusantara berdasarkan kata kunci tertentu. Aplikasi ini menggunakan **BM25** sebagai algoritma pencarian untuk menemukan resep yang paling relevan.

---

## 🎯 Fitur
- **Pencarian Resep:** Temukan resep makanan Nusantara berdasarkan kata kunci, seperti "ayam", "ikan", "telur", dll.
- **Rekomendasi Top 10:** Aplikasi memberikan 10 rekomendasi resep terbaik berdasarkan kata kunci.
- **Detail Resep:** Klik pada nama resep untuk melihat bahan-bahan dan langkah-langkah memasaknya.

---

## 🚀 Teknologi yang Digunakan
- **Python**
- **Streamlit**: Untuk membangun antarmuka pengguna.
- **rank-bm25**: Untuk melakukan pencarian berbasis teks menggunakan algoritma BM25.
- **Pandas**: Untuk memproses data dalam bentuk DataFrame.

---

## 📂 Struktur Dataset
Dataset terdiri dari beberapa file resep berdasarkan kategori bahan utama (misalnya ayam, ikan, sapi, dll.). File-file ini digabung menjadi satu DataFrame gabungan untuk mempermudah pencarian.

**Kolom penting dalam dataset:**
- `Title`: Judul resep.
- `clean_instructions`: Langkah-langkah memasak yang telah diproses.
- `Ingredients`: Daftar bahan-bahan resep.
- `Steps`: Langkah-langkah memasak dalam bentuk teks.

---

## 🛠️ Instalasi dan Menjalankan Aplikasi
1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username/resep-makanan-nusantara.git
   cd resep-makanan-nusantara
   ```
2. Install dependencies: Pastikan Anda memiliki Python 3.7+ dan jalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
3. Letakkan file dataset:
   - Tempatkan file pickle dataset di folder model
   - Pastikan penamaan file model nya benar
   
5. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```
6. Buka aplikasi di browser:
   Aplikasi akan berjalan di http://localhost:8501

---

## 🧩 Cara Penggunaan
1. Masukkan kata kunci pencarian pada kolom teks (contoh: "ayam").
2. Lihat daftar rekomendasi Top 10 yang relevan.
3. Klik salah satu nama resep untuk melihat bahan dan langkah memasak.

---

## 📝 Catatan
- Data resep harus dalam format pickle (.pkl) dan memiliki kolom sesuai dengan deskripsi di atas.
- Kode ini dirancang untuk mendukung resep dengan langkah-langkah dalam format list of lists.

---

## ❤️ Credits
Dibuat dengan ❤️ oleh Kelompok 5 MK Temu Kembali Informasi 2024 | UNSRI FASILKOM 2021
- Hafiz Muhammad Kurniawan 09021182126003
- Aisyah Nur Khoirofiq 09021182126004
- Shatia Earlangga Pratama 09021182126017
- Nur Su’udiyah 09021182126020
- Ana Safira 09021182126025
- Tri Yogta Rahmadhan 09021182126026
- Aditya Kurniawan 09021182126028


