import streamlit as st
import py3Dmol
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import AllChem
from scripts.engine import BarrieEngine
from scripts.validators import check_barrier_ratio

# --- Konfigurasi UI ---
st.set_page_config(page_title="Barriè | Dermal Design", layout="wide")
st.title("🧪 Barriè: Rational Dermal Design")
st.markdown("---")

# --- Backend Engine ---
engine = BarrieEngine()

# --- Sidebar Input ---
st.sidebar.header("Input Parameter")
ph = st.sidebar.slider("Target pH Kulit", 4.0, 7.0, 5.2)
ingredient = st.sidebar.selectbox("Bahan Aktif", ["Ceramide_NP", "Salicylic_Acid", "Niacinamide"])

# Database SMILES untuk visualisasi
smiles_db = {
    "Ceramide_NP": "CCCCCCCCCCCCCCCC(=O)NC[C@@H](O)[C@H](O)CO",
    "Salicylic_Acid": "C1=CC=C(C(=C1)C(=O)O)O",
    "Niacinamide": "C1=CN=CC=C1C(=O)N"
}

# --- Main Layout ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Analisis Kinetika")
    if st.button("Run Analysis"):
        # Layer 1: Validasi Rasio
        is_valid, status = check_barrier_ratio(3, 1, 1)
        
        if is_valid:
            # Layer 2: Prediksi
            res, _ = engine.predict_kinetics(ingredient, ph)
            if res:
                st.success(f"Status: {res['status']}")
                st.write(f"**Enzim Target:** {res['enzyme']}")
                st.write(f"**Km (Affinity):** {res['km']}")
                st.write(f"**Adjusted kcat:** {res['adjusted_kcat']}")
            else:
                st.error("Error: Engine failed to predict.")
        else:
            st.error(status)

with col2:
    st.subheader("Visualisasi 3D")
    def render_mol(smiles):
        # Generate 3D dari SMILES
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            mol = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol)
            pdb_block = Chem.MolToPDBBlock(mol)
            
            # Setup Viewer
            view = py3Dmol.view(width=400, height=400)
            view.addModel(pdb_block, 'pdb')
            view.setStyle({'stick': {}})
            view.zoomTo()
            # Render ke Web
            showmol(view, height=400, width=400)
        else:
            st.error("Gagal merender molekul.")
    
    render_mol(smiles_db[ingredient])
