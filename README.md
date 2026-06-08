# 🎓 SipaKu - Sistem Pakar Rekomendasi Jurusan Kuliah UTB

> **Tugas Kelompok Sistem Pakar menggunakan Metode Forward Chaining**  
> Universitas Teknologi Bandung (UTB)

Aplikasi sistem pakar berbasis web ini dirancang untuk merekomendasikan program studi di Universitas Teknologi Bandung (UTB) berdasarkan kelayakan nilai rapor sekolah (aspek kuantitatif) dan minat/bakat (aspek kualitatif) calon mahasiswa menggunakan mesin inferensi **Forward Chaining**.

---

## 📁 Struktur File

```
sistem_pakar/
├── app.py            → Flask backend + engine Forward Chaining
├── rules.py          → Knowledge base (5 jurusan UTB, aturan produksi, kriteria)
├── static/
│   └── images/
│       ├── logo-kotak.png   → Logo UTB vertikal (logo atas, text bawah)
│       └── logo-panjang.png → Logo UTB horizontal (logo samping, text samping)
├── templates/
│   ├── index.html    → Halaman utama / landing page (UTB theme)
│   ├── konsultasi.html → Halaman konsultasi (2-Step Stepper & Boolean input)
│   └── hasil.html    → Halaman hasil rekomendasi + penjelasan pakar
└── README.md
```

---

## ⚙️ Cara Menjalankan

Proyek ini telah dilengkapi dengan virtual environment (`env`) lokal.

### 1. Jalankan aplikasi menggunakan virtual environment

Buka terminal di direktori `sistem_pakar` lalu jalankan perintah:

```bash
env/bin/python3 app.py
```

### 2. Buka browser

Buka tautan berikut di peramban Anda:
```
http://127.0.0.1:5000
```

---

## 🧠 Cara Kerja Forward Chaining

Sistem bekerja secara deduktif, dimulai dari **FAKTA** yang diberikan oleh user (Langkah 1: Kelayakan Nilai Rapor SMA, Langkah 2: Kriteria Minat & Bakat), lalu mencocokkannya dengan **RULE BASE** (Aturan Produksi) menggunakan operator konjungsi ($\land$) untuk mencapai **KESIMPULAN** (Rekomendasi Jurusan).

### Contoh Rule:
- **Rule 1 (Teknik Informatika):** `(K01 ⋀ K04) ⋀ N01 → J01`
  * *IF Suka Logika (K01) AND Tertarik Teknologi (K04) AND Nilai Rapor Matematika ≥ 80 (N01) THEN Teknik Informatika (J01)*

- **Proses:** Sistem mencocokkan fakta-fakta yang dipilih user. Jika semua kriteria (K01, K04, N01) bernilai `TRUE`, maka jurusan **Teknik Informatika** akan dibuktikan dan direkomendasikan beserta penjelasan alasan pakar.

---

## 📊 Scope Sistem

| Aspek             | Detail                                                       |
| ----------------- | ------------------------------------------------------------ |
| **Jumlah Jurusan**    | 5 Jurusan UTB (TI, Industri, DKV, Bisnis Digital, Ritel)     |
| **Jumlah Kriteria**   | 10 Kriteria (6 Minat/Bakat, 4 Nilai Rapor)                   |
| **Aspek Penilaian**   | Kelayakan Akademik (Nilai Rapor ≥ 80) dan Minat & Bakat      |
| **Metode Inferensi**  | Forward Chaining                                             |
| **Tampilan UI**       | Modern Blue-Green (Identitas Kampus UTB), 2-Step Stepper     |

### Daftar Program Studi UTB:
1. **Teknik Informatika (J01)**
2. **Teknik Industri (J02)**
3. **Desain Komunikasi Visual / DKV (J03)**
4. **Bisnis Digital (J04)**
5. **Manajemen Retail (J05)**

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
