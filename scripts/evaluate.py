# scripts/evaluate.py

import os
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, 'outputs', 'predictions.csv')

# Load predictions
df = pd.read_csv(OUTPUT_PATH)

# Metrics
y_true = df['failure']
y_pred = df['predicted_failure']

print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))
print("\nClassification Report:")
print(classification_report(y_true, y_pred))
# Script for evaluation
