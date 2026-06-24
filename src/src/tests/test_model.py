import unittest
from src.model import ProteinLigandModel
import numpy as np

class TestProteinLigandModel(unittest.TestCase):
    def setUp(self):
        self.model = ProteinLigandModel()
    
    def test_model_creation(self):
        """Test if model creates successfully"""
        self.assertIsNotNone(self.model)
        self.assertFalse(self.model.is_trained)
    
    def test_model_training(self):
        """Test if model can train"""
        X_train = np.random.rand(10, 5)
        y_train = np.random.rand(10)
        self.model.train(X_train, y_train)
        self.assertTrue(self.model.is_trained)

if __name__ == '__main__':
    unittest.main()
