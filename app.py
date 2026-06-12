from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# 1. Definisi Gejala (Symptoms)
SYMPTOMS = {
    "G01": "Bercak hitam melingkar di daun",
    "G02": "Daun menguning dan rontok",
    "G03": "Lapisan putih seperti tepung menutupi daun dan kuncup bunga",
    "G04": "Bintik-bintik jingga atau karat di bagian bawah daun",
    "G05": "Batang coklat kehitaman",
    "G06": "Tanaman layu tiba-tiba",
    "G07": "Daun belang hijau muda-hijau tua seperti mozaik",
    "G08": "Kawanan kutu hijau kecil di pucuk dan kuncup bunga",
    "G09": "Kelopak bunga bercak keperakan",
    "G10": "Kuncup gagal mekar",
    "G11": "Jaring halus di bawah daun",
    "G12": "Daun kuning dan berbintik",
    "G13": "Daun muda kuning",
    "G14": "Tulang daun tetap hijau (klorosis)",
    "G15": "Daun bolong-bolong",
    "G16": "Kelopak bunga tergigit",
    "G17": "Terlihat ulat di sekitar tanaman"
}

# Pengelompokan Gejala untuk memudahkan UI
SYMPTOM_CATEGORIES = {
    "Gejala pada Daun": ["G01", "G02", "G03", "G04", "G07", "G11", "G12", "G13", "G14", "G15"],
    "Gejala pada Batang & Tanaman": ["G05", "G06"],
    "Gejala pada Bunga & Kuncup": ["G08", "G09", "G10", "G16"],
    "Gejala Hama Fisik": ["G17"]
}

# 2. Definisi Penyakit & Hama (Diseases & Pests Database)
DISEASES = {
    "P01": {
        "name": "Bercak Hitam (Black Spot)",
        "description": "Bercak Hitam (Black Spot) disebabkan oleh jamur Diplocarpon rosae. Penyakit ini sangat umum terjadi pada tanaman mawar terutama pada kondisi lembap dan hangat. Jika dibiarkan, daun akan menguning lalu rontok, yang melemahkan tanaman secara keseluruhan.",
        "symptoms": ["G01", "G02"],
        "treatment": {
            "immediate": [
                "Pangkas dan musnahkan daun yang terinfeksi (jangan dijadikan kompos).",
                "Semprotkan fungisida organik berbahan tembaga atau sulfur secara berkala.",
                "Hindari menyiram daun di sore/malam hari untuk mengurangi kelembapan permukaan daun."
            ],
            "prevention": [
                "Jaga kebersihan area sekitar tanaman dari guguran daun mawar yang busuk.",
                "Lakukan pemangkasan rutin agar sirkulasi udara di sekitar tajuk tanaman lancar.",
                "Pilih varietas mawar yang lebih tahan terhadap penyakit bercak hitam."
            ]
        }
    },
    "P02": {
        "name": "Embun Tepung (Powdery Mildew)",
        "description": "Embun Tepung (Powdery Mildew) disebabkan oleh jamur Podosphaera pannosa. Jamur ini menyukai kondisi hangat dan kering di siang hari serta lembap di malam hari. Gejalanya ditandai dengan munculnya lapisan putih berdebu pada daun, batang, dan kuncup.",
        "symptoms": ["G03"],
        "treatment": {
            "immediate": [
                "Pangkas bagian tanaman yang diselimuti lapisan putih tebal.",
                "Semprot dengan campuran baking soda (1 sendok teh) dan air (1 liter) ditambah beberapa tetes sabun cuci piring cair sebagai surfaktan, atau gunakan fungisida komersial."
            ],
            "prevention": [
                "Pastikan tanaman mendapatkan sinar matahari langsung minimal 6 jam sehari.",
                "Hindari penyiraman dari atas kepala (overhead watering) yang menyisakan kelembapan di daun."
            ]
        }
    },
    "P03": {
        "name": "Karat Daun (Rust)",
        "description": "Karat Daun disebabkan oleh jamur Phragmidium mucronatum. Penyakit ini memicu pembentukan pustul (bintik menonjol) berwarna jingga terang atau karat di bagian bawah daun, yang lama-kelamaan membuat daun gugur.",
        "symptoms": ["G04", "G02"],
        "treatment": {
            "immediate": [
                "Petik segera daun yang memiliki bintik jingga di bagian bawahnya.",
                "Aplikasikan fungisida berbahan aktif mankozeb atau sulfur."
            ],
            "prevention": [
                "Siram tanaman pada bagian akar/tanah, bukan pada daun.",
                "Bersihkan sisa tanaman di permukaan tanah secara berkala untuk memutus siklus hidup jamur."
            ]
        }
    },
    "P04": {
        "name": "Busuk Batang (Stem Rot)",
        "description": "Busuk Batang disebabkan oleh infeksi jamur seperti Coniothyrium wernsdorffiae atau bakteri patogen. Penyakit ini sering masuk melalui luka bekas pemangkasan. Batang akan berubah menjadi cokelat kehitaman dan tanaman layu tiba-tiba.",
        "symptoms": ["G05", "G06"],
        "treatment": {
            "immediate": [
                "Potong batang yang membusuk hingga ke bagian yang masih sehat (berwarna putih/hijau di dalamnya).",
                "Oleskan fungisida pasta atau lilin penutup luka pada bekas potongan untuk mencegah infeksi ulang."
            ],
            "prevention": [
                "Selalu sterilkan alat pangkas menggunakan alkohol 70% sebelum dan sesudah digunakan.",
                "Lakukan pemangkasan pada hari yang kering dan cerah."
            ]
        }
    },
    "P05": {
        "name": "Virus Mosaik (Mosaic Virus)",
        "description": "Virus Mosaik Mawar (Rose Mosaic Virus) ditularkan secara vegetatif melalui penyambungan (grafting) atau alat pemotongan yang tidak steril. Daun akan memperlihatkan pola belang hijau muda dan hijau tua yang khas seperti mosaik dan menurunkan estetika bunga.",
        "symptoms": ["G07"],
        "treatment": {
            "immediate": [
                "Tidak ada obat kimia untuk virus tanaman. Jika infeksi parah, tanaman harus dimusnahkan agar tidak menular ke mawar lain.",
                "Jika infeksi ringan, pertahankan tanaman namun pangkas bagian yang menunjukkan gejala berat."
            ],
            "prevention": [
                "Hanya gunakan bahan stek/grafting dari tanaman induk yang terjamin sehat bebas virus.",
                "Sterilkan gunting pangkas secara konsisten."
            ]
        }
    },
    "P06": {
        "name": "Kutu Daun (Aphids)",
        "description": "Kutu Daun (Aphids) adalah hama serangga kecil lunak berwarna hijau atau hitam yang mengisap cairan tanaman. Mereka biasanya bergerombol di bagian pucuk daun muda dan kuncup bunga mawar, menyebabkan tanaman kerdil.",
        "symptoms": ["G08", "G10"],
        "treatment": {
            "immediate": [
                "Semprot kawanan kutu daun dengan aliran air bertekanan kuat untuk menjatuhkannya.",
                "Gunakan semprotan sabun insektisida atau minyak neem (neem oil) pada pucuk tanaman."
            ],
            "prevention": [
                "Dukung kehadiran predator alami seperti kumbang koksi (ladybugs).",
                "Hindari pemupukan nitrogen berlebih yang memicu pertumbuhan daun muda terlalu subur (sangat disukai kutu daun)."
            ]
        }
    },
    "P07": {
        "name": "Thrips",
        "description": "Thrips adalah hama berukuran sangat kecil yang mengisap sel-sel kelopak bunga mawar. Mengakibatkan bercak keperakan atau kecokelatan pada kelopak bunga dan kuncup bunga gagal mekar dengan sempurna.",
        "symptoms": ["G09", "G10"],
        "treatment": {
            "immediate": [
                "Pangkas kuncup bunga yang rusak berat dan buang jauh-jauh.",
                "Semprotkan insektisida nabati atau spinosad di pagi atau sore hari."
            ],
            "prevention": [
                "Pasang perangkap lengket berwarna kuning (yellow sticky traps) di dekat tanaman.",
                "Jaga kelembapan tanah di sekitar tanaman mawar."
            ]
        }
    },
    "P08": {
        "name": "Tungau Merah (Spider Mites)",
        "description": "Tungau Merah (Tetranychidae) berkembang biak sangat cepat dalam kondisi kering dan panas. Mereka membuat jaring halus di bawah permukaan daun dan mengisap cairan sel, sehingga daun menjadi kuning berbintik dan akhirnya rontok.",
        "symptoms": ["G11", "G12"],
        "treatment": {
            "immediate": [
                "Semprot bagian bawah daun dengan air bertekanan tinggi secara rutin untuk merusak sarang jaring mereka.",
                "Aplikasikan akarisida organik atau minyak hortikultura."
            ],
            "prevention": [
                "Jaga kelembapan di sekitar tanaman dengan penyemprotan kabut (misting) air di siang hari yang terik.",
                "Mulsa tanah untuk mempertahankan kelembapan."
            ]
        }
    },
    "P09": {
        "name": "Kekurangan Zat Besi (Fe)",
        "description": "Kekurangan Zat Besi (Klorosis) bukan disebabkan patogen melainkan masalah nutrisi. Terjadi akibat pH tanah terlalu tinggi sehingga besi terikat dan tidak bisa diserap akar. Daun muda menguning sementara tulang daun tetap hijau.",
        "symptoms": ["G13", "G14"],
        "treatment": {
            "immediate": [
                "Berikan pupuk daun (foliar spray) zat besi kelat (Iron Chelate) langsung ke daun untuk penanganan cepat.",
                "Taburkan belerang/sulfur ke tanah untuk menurunkan pH tanah jika tanah terlalu alkalis."
            ],
            "prevention": [
                "Lakukan uji pH tanah dan jaga pH tanah mawar tetap ideal (antara 6.0 - 6.5).",
                "Tambahkan bahan organik seperti kompos untuk memperbaiki struktur dan kesuburan tanah."
            ]
        }
    },
    "P10": {
        "name": "Hama Ulat (Caterpillar)",
        "description": "Hama Ulat memakan dedaunan dan kelopak bunga mawar secara fisik. Daun akan terlihat bolong-bolong tidak beraturan dan kelopak bunga tampak tergigit. Ulat biasanya bersembunyi di balik daun atau dalam gulungan daun.",
        "symptoms": ["G15", "G16", "G17"],
        "treatment": {
            "immediate": [
                "Ambil ulat secara manual (handpicking) dan musnahkan.",
                "Semprot tanaman dengan bio-insektisida berbahan aktif Bacillus thuringiensis (Bt) yang aman bagi lingkungan."
            ],
            "prevention": [
                "Periksa tanaman mawar secara berkala, terutama di bawah daun dan sekitar pucuk.",
                "Jaga kebersihan kebun dari gulma yang bisa menjadi inang kupu-kupu bertelur."
            ]
        }
    }
}

# 3. Bobot Aturan Kepakaran (Certainty Factor Expert Rules)
# Menunjukkan tingkat keyakinan pakar bahwa gejala Gx mengindikasikan penyakit Px
EXPERT_CF = {
    "P01": {"G01": 0.90, "G02": 0.50},
    "P02": {"G03": 0.95},
    "P03": {"G04": 0.90, "G02": 0.40},
    "P04": {"G05": 0.90, "G06": 0.80},
    "P05": {"G07": 0.95},
    "P06": {"G08": 0.85, "G10": 0.40},
    "P07": {"G09": 0.85, "G10": 0.70},
    "P08": {"G11": 0.90, "G12": 0.60},
    "P09": {"G13": 0.80, "G14": 0.90},
    "P10": {"G15": 0.80, "G16": 0.80, "G17": 0.95}
}

@app.route('/')
def index():
    return render_template('index.html', diseases=DISEASES)

@app.route('/diseases')
def diseases():
    return render_template('diseases.html', diseases=DISEASES, symptoms_dict=SYMPTOMS)

@app.route('/diagnose', methods=['GET', 'POST'])
def diagnose():
    if request.method == 'POST':
        # Mengambil input gejala dan tingkat keyakinan dari form
        user_inputs = {}
        for symptom_id in SYMPTOMS.keys():
            val = request.form.get(symptom_id)
            if val:
                user_inputs[symptom_id] = float(val)
            else:
                user_inputs[symptom_id] = 0.0

        # Filter gejala yang dipilih (CF > 0)
        selected_symptoms = {k: v for k, v in user_inputs.items() if v > 0}

        if not selected_symptoms:
            return render_template('diagnose.html', 
                                   categories=SYMPTOM_CATEGORIES, 
                                   symptoms=SYMPTOMS, 
                                   error="Pilihlah minimal satu gejala untuk mendiagnosis tanaman mawar Anda.")

        # --- A. METODE FORWARD CHAINING ---
        # Mencari penyakit kandidat yang minimal memiliki satu gejala yang dialami pengguna
        candidates = []
        rule_triggers = [] # Untuk dokumentasi inferensi
        
        for p_code, p_info in DISEASES.items():
            matched_symptoms_for_disease = [g for g in p_info["symptoms"] if g in selected_symptoms]
            if matched_symptoms_for_disease:
                candidates.append(p_code)
                # Catat aturan yang terpicu
                rule_text = f"IF ({' OR '.join([SYMPTOMS[g] for g in p_info['symptoms']])}) THEN Kemungkinan {p_info['name']}"
                triggered_by = ", ".join([SYMPTOMS[g] for g in matched_symptoms_for_disease])
                rule_triggers.append({
                    "disease_name": p_info["name"],
                    "rule": rule_text,
                    "triggered_by": triggered_by
                })

        # --- B. METODE CERTAINTY FACTOR ---
        diagnosis_results = []
        inference_steps = {}

        for p_code in candidates:
            p_info = DISEASES[p_code]
            rules_cf = EXPERT_CF[p_code]
            
            # Cari gejala penyakit ini yang diinput oleh pengguna
            active_symptoms = []
            steps = []
            
            for g_code in p_info["symptoms"]:
                if g_code in selected_symptoms:
                    cf_user = selected_symptoms[g_code]
                    cf_expert = rules_cf[g_code]
                    cf_calc = cf_user * cf_expert
                    active_symptoms.append(cf_calc)
                    steps.append({
                        "symptom": SYMPTOMS[g_code],
                        "cf_user": cf_user,
                        "cf_expert": cf_expert,
                        "cf_calc": round(cf_calc, 4)
                    })
            
            # Hitung kombinasi Certainty Factor
            cf_combine = 0.0
            if active_symptoms:
                cf_combine = active_symptoms[0]
                combination_log = [f"CF₁ = {round(cf_combine, 4)}"]
                
                for idx, cf_next in enumerate(active_symptoms[1:], start=2):
                    old_cf = cf_combine
                    cf_combine = old_cf + cf_next * (1.0 - old_cf)
                    combination_log.append(
                        f"CF_combine({idx}) = {round(old_cf, 4)} + {round(cf_next, 4)} * (1.0 - {round(old_cf, 4)}) = {round(cf_combine, 4)}"
                    )
                
                inference_steps[p_code] = {
                    "steps": steps,
                    "combination_log": combination_log,
                    "final_cf": round(cf_combine, 4)
                }

                diagnosis_results.append({
                    "code": p_code,
                    "name": p_info["name"],
                    "cf": cf_combine,
                    "percentage": round(cf_combine * 100, 2),
                    "description": p_info["description"],
                    "treatment": p_info["treatment"]
                })

        # Urutkan berdasarkan Certainty Factor tertinggi
        diagnosis_results = sorted(diagnosis_results, key=lambda x: x["cf"], reverse=True)

        return render_template('results.html', 
                               results=diagnosis_results, 
                               selected_symptoms=selected_symptoms,
                               symptoms_dict=SYMPTOMS,
                               rule_triggers=rule_triggers,
                               inference_steps=inference_steps,
                               diseases=DISEASES)

    return render_template('diagnose.html', categories=SYMPTOM_CATEGORIES, symptoms=SYMPTOMS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
