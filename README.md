# Protein-Ligand Model

A machine learning model to predict protein complex interactions and ligand binding.

## Features
- Load and parse PDB protein structures
- Extract molecular features
- Predict ligand-protein binding affinity
- Visualize interactions

## Installation

```bash
git clone https://github.com/janney7006-max/Protien-ligand-model.git
cd Protien-ligand-model
pip install -r requirements.txt
```

## Usage

```python
from src.predictor import predict_binding
result = predict_binding(protein_file, ligand_file)
```

## Data Sources
- PDB: https://www.rcsb.org/
- ChEMBL: https://www.ebi.ac.uk/chembl/

## License
MIT
