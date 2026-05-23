from huggingface_hub import snapshot_download
import os

def download_model():
    model_name = "facebook/esm2_t6_8M_UR50D"
    local_dir = "models/esm2_base"
    
    print(f"Mengunduh model {model_name} ke folder {local_dir}...")
    snapshot_download(repo_id=model_name, local_dir=local_dir)
    print("Download model selesai!")

if __name__ == "__main__":
    download_model()