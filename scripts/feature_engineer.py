# scripts/feature_engineer.py

import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(ROOT, 'data', 'raw', 'manufacturing_data.csv')
DATA_PROCESSED = os.path.join(ROOT, 'data', 'processed', 'processed.csv')

# Load raw data
df = pd.read_csv(DATA_RAW)
print("Raw dataset shape:", df.shape)

# Feature Engineering
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df['dayofweek'] = pd.to_datetime(df['timestamp']).dt.dayofweek

# Drop timestamp (not used for modeling)
df_model = df.drop(columns=['timestamp'])

# Scale numerical features
num_cols = ['rpm', 'temperature', 'vibration', 'pressure', 'age']
scaler = StandardScaler()
df_model[num_cols] = scaler.fit_transform(df_model[num_cols])

# Save processed dataset
os.makedirs(os.path.join(ROOT,'data','processed'), exist_ok=True)
df_model.to_csv(DATA_PROCESSED, index=False)
print("Processed dataset saved to:", DATA_PROCESSED)
print(df_model.head())
