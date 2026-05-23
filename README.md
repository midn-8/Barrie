# Barriè: A Computational Framework for Kinetic-Tuned Dermal Design

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research-Phase](https://img.shields.io/badge/status-active-green.svg)]()

Barriè adalah kerangka kerja komputasi (computational framework) inovatif yang menjembatani **biokimia kulit (dermatologi)** dengan **Bioinformatics Deep Learning**. Proyek ini bertujuan untuk mentransformasi pengembangan produk *skincare* dari pendekatan empiris (*trial-and-error*) menjadi desain rasional berbasis kinetika enzimatis (*Rational Dermal Design*).

---

## 🎯 Visi Riset
Industri kosmetik saat ini sangat bergantung pada evaluasi visual dan pengujian subyektif. Barriè mengintervensi proses ini dengan menyediakan **Virtual Dermal Simulation**—memprediksi bagaimana bahan aktif (SMILES) berinteraksi dengan jalur enzimatik alami kulit ($K_m$ dan $k_{cat}$) sebelum formula diuji di laboratorium (*wet-lab*).

## 🔬 Core Innovations
Barriè tidak hanya menggunakan model AI yang sudah ada, tetapi melakukan **Domain Adaptation** untuk dermatologi melalui:
*   **Dermal-Kinetome Dataset:** Kurasi data enzim spesifik *stratum corneum* (KLK5, KLK7, GBA1, SOD) yang belum terintegrasi di dataset publik.
*   **Conditional Deep Learning:** Modifikasi arsitektur *dual-encoder* (berbasis EnzyCLIP) dengan penambahan *pH-constraint layer* untuk menyesuaikan prediksi dengan kondisi fisiologis kulit (pH 4.7–5.5).
*   **Triple-Axis Validation:** Evaluasi komprehensif pada tiga pilar kesehatan kulit:
    1.  **Barrier Integrity** (Lipid synthesis).
    2.  **Healthy Exfoliation** (Proteolytic desquamation).
    3.  **Antioxidant Defense** (Redox homeostasis).

## 🏗 Pipeline Kerja
Barriè beroperasi melalui dua lapisan validasi:
1.  **Macro-Level (Rule-Based):** Mengecek integritas formulasi dasar berdasarkan prinsip fisiologis lipid (rasio 3:1:1).
2.  **Micro-Level (Kinetic Inference):** Menggunakan *Deep Learning* untuk memprediksi efikasi kinetik bahan aktif pada enzim kulit target.

## 🛠 Instalasi
```bash
# Clone repository
git clone [https://github.com/midn-8/Barrie.git](https://github.com/midn-8/Barrie.git)

# Install dependencies
pip install -r requirements.txt

# Persiapan dataset Dermal-Kinetome
python scripts/curate_dataset.py --source uniprot
