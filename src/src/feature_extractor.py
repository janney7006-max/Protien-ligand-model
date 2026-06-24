import numpy as np

class FeatureExtractor:
    def __init__(self):
        pass
    
    def extract_protein_features(self, structure):
        """Extract features from protein structure"""
        atoms = list(structure.get_atoms())
        residues = list(structure.get_residues())
        
        features = {
            'num_atoms': len(atoms),
            'num_residues': len(residues),
            'center_of_mass': self._calculate_center_of_mass(atoms)
        }
        return features
    
    def _calculate_center_of_mass(self, atoms):
        """Calculate center of mass"""
        coords = np.array([atom.get_coord() for atom in atoms])
        return np.mean(coords, axis=0).tolist()
