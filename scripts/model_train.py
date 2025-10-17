# scripts/model_train.py

import os
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PROCESSED = os.path.join(ROOT, 'data', 'processed', 'processed.csv')
MODEL_PATH = os.path.join(ROOT, 'models', 'xgb_model.pkl')

os.makedirs(os.path.join(ROOT,'models'), exist_ok=True)

# Load processed data
df = pd.read_csv(DATA_PROCESSED)

# Features & target
X = df.drop(columns=['failure'])
y = df['failure']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train XGBoost
model = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1, use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, MODEL_PATH)
print(f"Trained model saved to {MODEL_PATH}")
# Script for training model
