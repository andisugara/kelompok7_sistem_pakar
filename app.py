from flask import Flask, render_template, request, session, redirect, url_for
from rules import RULES, PERTANYAAN_MINAT, PERTANYAAN_MAPEL
import json

app = Flask(__name__)
app.secret_key = "sistempakar_utb_2026"

# Display names for the collected facts on the results page
DISPLAY_FAKTA = {
    "K01": "Suka Logika, Matematika & Coding",
    "K02": "Suka Sistem Kerja & Efisiensi",
    "K03": "Suka Seni Visual & Desain",
    "K04": "Tertarik Teknologi & Komputer",
    "K05": "Tertarik Bisnis & Startup",
    "K06": "Suka Analisis Pasar & Ritel",
    "N01": "Nilai Rapor Matematika ≥ 80",
    "N02": "Nilai Rapor Bahasa Inggris ≥ 80",
    "N03": "Nilai Rapor Ekonomi ≥ 80",
    "N04": "Nilai Rapor Seni Budaya ≥ 80"
}

# ============================================================
# ENGINE FORWARD CHAINING
# ============================================================

def forward_chaining(jurusan, fakta_user):
    """
    Forward Chaining: Cek apakah fakta user memenuhi 
    kondisi (rule) dari jurusan tersebut.
    """
    rule = RULES.get(jurusan)
    if not rule:
        return False, []

    for kondisi_set in rule["kondisi"]:
        terpenuhi = all(k in fakta_user for k in kondisi_set)
        if terpenuhi:
            return True, kondisi_set

    return False, []


def hitung_skor(jurusan, fakta_user):
    """
    Hitung skor kesesuaian jurusan berdasarkan berapa banyak
    kondisi yang terpenuhi dari rule set jurusan tersebut (K01-K06, N01-N04).
    """
    rule = RULES.get(jurusan)
    if not rule:
        return 0

    # Di skema baru, masing-masing jurusan memiliki tepat 1 kondisi_set (3 kondisi)
    kondisi_set = rule["kondisi"][0]
    total_kondisi = len(kondisi_set)
    terpenuhi = sum(1 for k in kondisi_set if k in fakta_user)

    if total_kondisi == 0:
        return 0
    return round((terpenuhi / total_kondisi) * 100, 1)


def generate_alasan(kondisi_terpenuhi):
    """
    Menghasilkan penjelasan pakar yang natural berdasarkan kondisi yang terpenuhi.
    Sesuai dengan spesifikasi dokumen laporan.
    """
    LABELS = {
        "K01": "Logika (K01)",
        "K02": "Sistem Kerja (K02)",
        "K03": "Seni Visual (K03)",
        "K04": "Teknologi (K04)",
        "K05": "Bisnis (K05)",
        "K06": "Analisis Pasar (K06)",
        "N01": "Matematika (N01)",
        "N02": "Bahasa Inggris (N02)",
        "N03": "Ekonomi (N03)",
        "N04": "Seni Budaya (N04)"
    }
    
    interests = [LABELS[k] for k in kondisi_terpenuhi if k.startswith('K') and k in LABELS]
    grades = [LABELS[k] for k in kondisi_terpenuhi if k.startswith('N') and k in LABELS]
    
    parts = []
    if interests:
        parts.append("kamu memiliki minat kuat di bidang " + " & ".join(interests))
    if grades:
        parts.append("Nilai " + " & ".join(grades) + " kamu memenuhi syarat minimal")
        
    if len(parts) == 2:
        return f"Sistem merekomendasikan jurusan ini karena {parts[0]}, serta {parts[1]}."
    elif len(parts) == 1:
        return f"Sistem merekomendasikan jurusan ini karena {parts[0]}."
    return "Sistem merekomendasikan jurusan ini berdasarkan kriteria yang terpenuhi."


def generate_rekomendasi(fakta_user):
    """
    Jalankan Forward Chaining untuk semua jurusan,
    kembalikan daftar jurusan yang cocok beserta skor dan penjelasan pakar.
    """
    hasil = []

    for jurusan in RULES:
        terbukti, kondisi_terpenuhi = forward_chaining(jurusan, fakta_user)
        skor = hitung_skor(jurusan, fakta_user)

        if terbukti:
            explanation = generate_alasan(kondisi_terpenuhi)
            hasil.append({
                "jurusan": jurusan,
                "kode": RULES[jurusan]["kode"],
                "skor": skor,
                "kondisi_terpenuhi": kondisi_terpenuhi,
                "deskripsi": RULES[jurusan]["deskripsi"],
                "prospek": RULES[jurusan]["prospek"],
                "alasan": explanation
            })

    # Urutkan dari skor tertinggi (meski semua terbukti akan 100%, urutan tetap stabil)
    hasil.sort(key=lambda x: x["skor"], reverse=True)
    return hasil


# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def index():
    session.clear()
    return render_template("index.html")


@app.route("/mulai")
def mulai():
    return redirect(url_for("konsultasi"))


@app.route("/konsultasi", methods=["GET", "POST"])
def konsultasi():
    if request.method == "POST":
        fakta_user = []
        
        # 1. Ambil checkbox kelayakan nilai (N01 - N04) dan minat (K01 - K06)
        all_keys = ["N01", "N02", "N03", "N04", "K01", "K02", "K03", "K04", "K05", "K06"]
        for k in all_keys:
            if request.form.get(k):
                fakta_user.append(k)
                
        # 2. Susun data status kelayakan nilai untuk halaman hasil
        nilai_rapor = {
            "matematika": "≥ 80" if "N01" in fakta_user else "< 80",
            "binggris": "≥ 80" if "N02" in fakta_user else "< 80",
            "ekonomi": "≥ 80" if "N03" in fakta_user else "< 80",
            "seni": "≥ 80" if "N04" in fakta_user else "< 80"
        }
        
        # Simpan ke session
        session["fakta"] = fakta_user
        session["nilai_rapor"] = nilai_rapor
        
        return redirect(url_for("hasil"))
        
    return render_template("konsultasi.html", 
                           pertanyaan_minat=PERTANYAAN_MINAT, 
                           pertanyaan_mapel=PERTANYAAN_MAPEL)


@app.route("/hasil")
def hasil():
    if "fakta" not in session:
        return redirect(url_for("index"))

    fakta_user = session.get("fakta", [])
    nilai_rapor = session.get("nilai_rapor", {})
    rekomendasi = generate_rekomendasi(fakta_user)

    # Label fakta untuk ditampilkan di hasil
    label_fakta = [DISPLAY_FAKTA.get(f, f) for f in fakta_user]

    return render_template("hasil.html",
                           rekomendasi=rekomendasi,
                           fakta_user=fakta_user,
                           nilai_rapor=nilai_rapor,
                           label_fakta=label_fakta,
                           total_jurusan=len(RULES))


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
