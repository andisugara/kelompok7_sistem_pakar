# 🌹 RoseCare - Sistem Pakar Diagnosis Penyakit Mawar

**RoseCare** adalah aplikasi sistem pakar yang dirancang khusus untuk membantu petani atau pecinta tanaman mawar dalam mendiagnosis masalah pada tanaman mawar. Aplikasi ini mencakup **10 jenis penyakit dan hama utama** pada mawar.

---

## 📋 Daftar Penyakit & Hama Mawar

| No | Penyakit/Hama | Gejala |
|----|---------------|--------|
| 1 | Bercak Hitam (Black Spot) | Bercak hitam melingkar di daun, daun menguning dan rontok |
| 2 | Embun Tepung (Powdery Mildew) | Lapisan putih seperti tepung menutupi daun dan kuncup bunga |
| 3 | Karat Daun | Bintik-bintik jingga atau karat di bagian bawah daun |
| 4 | Busuk Batang | Batang coklat kehitaman, tanaman layu tiba-tiba |
| 5 | Virus Mosaik | Daun belang hijau muda-hijau tua seperti mozaik |
| 6 | Kutu Daun (Aphids) | Kawanan kutu hijau kecil di pucuk dan kuncup bunga |
| 7 | Thrips | Kelopak bunga bercak keperakan, kuncup gagal mekar |
| 8 | Tungau Merah | Jaring halus di bawah daun, daun kuning dan berbintik |
| 9 | Kekurangan Zat Besi (Fe) | Daun muda kuning, tulang daun tetap hijau (klorosis) |
| 10 | Hama Ulat | Daun bolong-bolong, kelopak bunga tergigit |

---

## 🧠 Metode Sistem Pakar

### a. Forward Chaining (Pelacakan ke Depan)
Metode ini bekerja dengan mengumpulkan gejala-gejala yang teramati pada tanaman mawar, kemudian menelusuri aturan-aturan yang ada untuk menentukan penyakit atau hama yang paling mungkin menyerang.

**Contoh:** Jika ditemukan gejala daun berlubang, kelopak bunga tergigit, dan terlihat ulat di sekitar tanaman, maka sistem akan menyimpulkan bahwa tanaman terserang **Hama Ulat**.

### b. Certainty Factor (Faktor Kepastian)
Metode ini digunakan untuk menangani ketidakpastian dalam diagnosis. Setiap gejala diberi nilai tingkat keyakinan oleh pengguna (0-1), kemudian sistem menghitung kombinasi nilai *Certainty Factor* untuk menentukan penyakit dengan tingkat keyakinan tertinggi.

**Contoh nilai keyakinan:**
- Yakin: 0.9
- Agak yakin: 0.6
- Tidak yakin: 0.2

---

## 🎯 Tujuan Aplikasi

Membantu pengguna mengenali masalah pada tanaman mawar secara:
- ✅ Cepat
- ✅ Praktis
- ✅ Akurat

Dengan mempertimbangkan tingkat ketidakpastian gejala yang diamati, serta memberikan **rekomendasi penanganan** yang sesuai untuk setiap kasus. Aplikasi ini sangat berguna bagi petani mawar maupun penghobi yang kesulitan mengakses tenaga ahli pertanian secara langsung.

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|----------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, Tailwind CSS |
| Logika Sistem Pakar | Forward Chaining & Certainty Factor |

---

## 🚀 Cara Menjalankan Aplikasi

```bash
# 1. Clone repository
git clone https://github.com/andisugara/rosecare.git
cd rosecare

# 2. Buat virtual environment (opsional tapi disarankan)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install flask

# 4. Jalankan aplikasi
python app.py

# 5. Buka browser dan akses
http://localhost:5000

---

## 👥 Anggota Kelompok

| No  | Nama                | NIM         |
| :-: | ------------------- | ----------- |
|  1  | Andi Sugara Putra   | 22552011093 |
|  2  | Chen Chen Juwita    | 22552011236 |
|  3  | Nada Ismaya         | 23552011125 |
|  4  | Naswa Mutiara       | 23552011185 |
|  5  | Nur Anisa           | 23552011171 |
|  6  | Samara Buana Tungga | 23552011126 |

---

## 👨‍🏫 Informasi Kelas

| Aspek              | Detail                              |
| ------------------ | ----------------------------------- |
| **Dosen Pengampu** | Iis Ismawati, M.Kom                 |
| **Kelas**          | TIF RM 22B                          |
| **Mata Kuliah**    | Sistem Pakar                        |
| **Universitas**    | Universitas Teknologi Bandung (UTB) |