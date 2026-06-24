from Bio.PDB import PDBParser

class ProteinLoader:
    def __init__(self):
        self.parser = PDBParser(QUIET=True)
    
    def load_pdb(self, pdb_file):
        """Load PDB protein structure file"""
        structure = self.parser.get_structure('protein', pdb_file)
        return structure
    
    def get_atoms(self, structure):
        """Get all atoms from protein"""
        atoms = list(structure.get_atoms())
        return atoms
