from sklearn.ensemble import RandomForestRegressor
import numpy as np

class ProteinLigandModel:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100)
        self.is_trained = False
    
    def train(self, X_train, y_train):
        """Train the model on features and binding affinities"""
        self.model.fit(X_train, y_train)
        self.is_trained = True
        print("Model trained successfully!")
    
    def predict(self, X_test):
        """Predict binding affinity"""
        if not self.is_trained:
            raise Exception("Model must be trained first!")
        return self.model.predict(X_test)
