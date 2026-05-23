import requests
import os

# Daftar target enzim riset Barriè
barrier_enzymes = {
    "KLK5": "Q9Y337",
    "KLK7": "P49862",
    "GBA1": "P04062",
    "KLK6": "Q92876"
}

def fetch_uniprot_fasta(name, uniprot_id):
    """Mengunduh sequence protein dari UniProt dalam format FASTA."""
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Cek apakah ada error HTTP
        
        # Lokasi penyimpanan: data/fasta/{name}.fasta
        folder_path = os.path.join("data", "fasta")
        os.makedirs(folder_path, exist_ok=True)
        
        filepath = os.path.join(folder_path, f"{name}.fasta")
        
        with open(filepath, "w") as f:
            f.write(response.text)
            
        print(f"[SUCCESS] {name} berhasil disimpan di {filepath}")
        
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Gagal mengunduh {name}: {e}")

if __name__ == "__main__":
    print("--- Memulai pengunduhan data FASTA ---")
    for name, uid in barrier_enzymes.items():
        fetch_uniprot_fasta(name, uid)
    print("--- Proses selesai ---")