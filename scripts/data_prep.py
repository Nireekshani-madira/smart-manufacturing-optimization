# scripts/data_prep.py
import os
import pandas as pd
import numpy as np

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(ROOT, 'data', 'raw', 'manufacturing_data.csv')

# Ensure folder exists
os.makedirs(os.path.join(ROOT, 'data', 'raw'), exist_ok=True)

# Generate synthetic dataset
print("Generating synthetic dataset...")
np.random.seed(42)
records = []
n_machines = 5
n_records_per = 500

for machine in range(n_machines):
    base_temp = 60 + np.random.randn()*2
    base_vib = 0.3 + abs(np.random.randn()*0.05)
    for t in range(n_records_per):
        timestamp = pd.Timestamp('2024-01-01') + pd.Timedelta(seconds=30*t)
        rpm = 1000 + 50*np.sin(t/50) + np.random.randn()*10
        temperature = base_temp + 0.05*np.sin(t/100) + np.random.randn()*0.5
        vibration = base_vib + 0.005*np.sin(t/10) + np.random.randn()*0.02
        pressure = 5 + 0.01*np.cos(t/20) + np.random.randn()*0.1
        age = np.random.randint(0, 1000)
        fail_prob = (vibration*10 + (temperature-60)*0.2 + age*0.0005)
        failure = 1 if np.random.rand() < min(max(fail_prob*0.01,0),0.5) else 0
        records.append((machine, timestamp, rpm, temperature, vibration, pressure, age, failure))

df = pd.DataFrame(records, columns=['machine_id','timestamp','rpm','temperature','vibration','pressure','age','failure'])

# Save dataset
df.to_csv(DATA_RAW, index=False)
print("Synthetic dataset saved to:", DATA_RAW)
print(df.head())
