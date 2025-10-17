# scripts/model_inference.py

import os
import pandas as pd
import joblib

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PROCESSED = os.path.join(ROOT, 'data', 'processed', 'processed.csv')
MODEL_PATH = os.path.join(ROOT, 'models', 'xgb_model.pkl')
OUTPUT_PATH = os.path.join(ROOT, 'outputs', 'predictions.csv')

os.makedirs(os.path.join(ROOT,'outputs'), exist_ok=True)

# Load processed data
df = pd.read_csv(DATA_PROCESSED)

# Load model
model = joblib.load(MODEL_PATH)

# Predict
X = df.drop(columns=['failure'])
y_true = df['failure']
y_pred = model.predict(X)
df['predicted_failure'] = y_pred

# Save predictions
df.to_csv(OUTPUT_PATH, index=False)
print("Predictions saved to:", OUTPUT_PATH)
print(df.head())
# Script for model inference
