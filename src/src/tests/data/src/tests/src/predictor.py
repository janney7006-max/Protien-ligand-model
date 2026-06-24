"""Main prediction interface for protein-ligand binding"""

from .data_loader import ProteinLoader
from .feature_extractor import FeatureExtractor
from .model import ProteinLigandModel
import yaml

class ProteinLigandPredictor:
    def __init__(self, config_path="config.yaml"):
        """Initialize predictor with configuration"""
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.loader = ProteinLoader()
        self.extractor = FeatureExtractor()
        self.model = ProteinLigandModel()
    
    def predict_binding(self, protein_file, ligand_file):
        """Predict binding affinity between protein and ligand"""
        
        # Load protein
        protein = self.loader.load_pdb(protein_file)
        
        # Extract features
        features = self.extractor.extract_protein_features(protein)
        
        # Make prediction
        # (simplified - in real version would combine protein + ligand features)
        prediction = {
            'protein_file': protein_file,
            'ligand_file': ligand_file,
            'binding_affinity': 0.85,  # placeholder
            'confidence': 0.92
        }
        
        return prediction
    
    def batch_predict(self, protein_files, ligand_files):
        """Predict binding for multiple protein-ligand pairs"""
        results = []
        for prot, lig in zip(protein_files, ligand_files):
            result = self.predict_binding(prot, lig)
            results.append(result)
        return results
