import os
import torch
from transformers import AutoTokenizer, AutoModel

class ProteinProcessor:
    def __init__(self):
        # Mengarah ke folder model yang sudah kita download
        self.model_path = os.path.join("models", "esm2_base")
        
        print(f"Memuat model dari: {self.model_path}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModel.from_pretrained(self.model_path)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        print(f"Model berhasil dimuat pada: {self.device}")

    def get_embedding(self, sequence):
        """Mengubah urutan FASTA menjadi vektor angka (embedding)"""
        inputs = self.tokenizer(sequence, return_tensors="pt", padding=True, truncation=True).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Mengambil rata-rata dari hidden states untuk mendapatkan representasi protein
        embedding = outputs.last_hidden_state.mean(dim=1)
        return embedding.cpu().numpy()

# Test load untuk memastikan processor bekerja
if __name__ == "__main__":
    proc = ProteinProcessor()
    # Test dengan sequence pendek
    test_seq = "MKTVRQERLKSIVR"
    vec = proc.get_embedding(test_seq)
    print(f"Shape vektor: {vec.shape}")
    print("Processor siap digunakan!")