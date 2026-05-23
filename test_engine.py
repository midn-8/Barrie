from scripts.engine import BarrieEngine

# 1. Inisialisasi engine (ini akan otomatis memuat model AI)
engine = BarrieEngine()

# 2. Coba jalankan prediksi untuk salah satu bahan
bahan = "Ceramide_NP"
data, pesan = engine.predict_kinetics(bahan, 5.5)

print(f"Hasil: {pesan}")
print(f"Data Bahan: {data}")
