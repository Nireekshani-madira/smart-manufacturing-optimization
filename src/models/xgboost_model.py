# src/models/xgboost_model.py
from xgboost import XGBClassifier
import joblib

class XGBoostModel:
    def __init__(self, n_estimators=100, max_depth=4, learning_rate=0.1):
        self.model = XGBClassifier(n_estimators=n_estimators,
                                   max_depth=max_depth,
                                   learning_rate=learning_rate,
                                   eval_metric='logloss')
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def save(self, path):
        joblib.dump(self.model, path)
    
    def load(self, path):
        self.model = joblib.load(path)
# XGBoost model wrapper
