# ============================================================
# KNOWLEDGE BASE - SISTEM PAKAR REKOMENDASI JURUSAN KULIAH
# Metode: Forward Chaining
# Dibuat untuk tugas Sistem Pakar - Universitas Teknologi Bandung (UTB)
# ============================================================

# Daftar semua jurusan yang bisa direkomendasikan
JURUSAN = [
    "Teknik Informatika",
    "Teknik Industri",
    "Desain Komunikasi Visual (DKV)",
    "Bisnis Digital",
    "Manajemen Retail",
]

# ============================================================
# RULE BASE
# Setiap jurusan punya daftar kondisi (fakta) yang harus terpenuhi
# Format: { "jurusan": { "kode": "Jxx", "deskripsi": "...", "prospek": "...", "kondisi": [[fakta1, fakta2, ...]] } }
#
# Kondisi mengacu pada key dari fakta user:
#   K01 - K06 : Minat & Bakat
#   N01 - N04 : Kelayakan Nilai Rapor
# ============================================================

RULES = {
    "Teknik Informatika": {
        "kode": "J01",
        "deskripsi": "Mempelajari pengembangan perangkat lunak, algoritma, kecerdasan buatan, keamanan siber, dan sistem komputer.",
        "prospek": "Software Engineer, Data Scientist, IT Consultant, Cybersecurity Specialist, Game Developer",
        "kondisi": [
            ["K01", "K04", "N01"]
        ]
    },
    "Teknik Industri": {
        "kode": "J02",
        "deskripsi": "Fokus pada perancangan, peningkatan, dan instalasi sistem terintegrasi yang terdiri dari manusia, material, peralatan, dan energi untuk meningkatkan efisiensi.",
        "prospek": "Industrial Engineer, Production Planner (PPIC), Quality Engineer, Supply Chain Analyst, Operations Manager",
        "kondisi": [
            ["K01", "K02", "N01"]
        ]
    },
    "Desain Komunikasi Visual (DKV)": {
        "kode": "J03",
        "deskripsi": "Mempelajari seni komunikasi menggunakan bahasa visual melalui desain grafis, ilustrasi, fotografi, videografi, dan multimedia interaktif.",
        "prospek": "Graphic Designer, UI/UX Designer, Illustrator, Video Editor, Brand Designer, Art Director",
        "kondisi": [
            ["K03", "K04", "N04"]
        ]
    },
    "Bisnis Digital": {
        "kode": "J04",
        "deskripsi": "Menggabungkan ilmu manajemen bisnis, e-commerce, pemasaran digital, dan teknologi informasi untuk menghadapi era ekonomi digital.",
        "prospek": "Digital Strategist, E-commerce Manager, Social Media Specialist, Business Development, Startup Founder",
        "kondisi": [
            ["K04", "K05", "N02"]
        ]
    },
    "Manajemen Retail": {
        "kode": "J05",
        "deskripsi": "Mempelajari pengelolaan bisnis ritel modern, analisis perilaku konsumen, manajemen rantai pasok ritel, merchandising, dan operasional toko.",
        "prospek": "Retail Store Manager, Merchandiser, Retail Buyer, Category Manager, Retail Marketing Analyst",
        "kondisi": [
            ["K05", "K06", "N03"]
        ]
    }
}

# ============================================================
# DAFTAR KRITERIA & PERTANYAAN
# ============================================================

PERTANYAAN_MINAT = {
    "K01": "Saya suka tantangan logika, matematika, atau coding.",
    "K02": "Saya tertarik mempelajari cara kerja pabrik, organisasi, dan efisiensi sistem.",
    "K03": "Saya hobi menggambar, membuat desain visual, atau dunia multimedia.",
    "K04": "Saya selalu penasaran dengan perkembangan teknologi gadget dan komputer.",
    "K05": "Saya tertarik dengan dunia bisnis, startup, dan cara menghasilkan uang.",
    "K06": "Saya suka menganalisis tren belanja orang dan cara mengelola toko."
}

PERTANYAAN_MAPEL = {
    "N01": "Matematika",
    "N02": "Bahasa Inggris",
    "N03": "Ekonomi / IPS",
    "N04": "Seni Budaya / Prakarya"
}
