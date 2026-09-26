import os
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

print("Creating dummy Crop Recommendation dataset...")

# Generate a small synthetic dataset for standard crops
data = [
    # N, P, K, temp, humidity, ph, rainfall, label
    [90, 42, 43, 20.8, 82.0, 6.5, 202.9, 'rice'],
    [85, 58, 41, 21.7, 80.3, 7.0, 226.6, 'rice'],
    [60, 55, 44, 23.0, 60.0, 5.5, 140.0, 'maize'],
    [70, 48, 53, 24.5, 65.0, 6.2, 120.0, 'maize'],
    [20, 134, 198, 27.0, 80.0, 5.7, 100.0, 'banana'],
    [100, 20, 30, 25.0, 60.0, 6.8, 80.0, 'watermelon'],
    [40, 60, 80, 18.0, 50.0, 7.2, 90.0, 'chickpea'],
    [105, 14, 50, 28.0, 75.0, 6.3, 180.0, 'jute'],
    [20, 25, 30, 26.0, 90.0, 6.7, 150.0, 'coconut'],
    [100, 35, 30, 24.0, 85.0, 6.4, 230.0, 'coffee']
]

columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'label']
df = pd.DataFrame(data, columns=columns)

X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

print("Training Random Forest Classifier...")
rf = RandomForestClassifier(n_estimators=10, random_state=42)
rf.fit(X, y)

model_filename = 'RF.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(rf, file)

print(f"Success! '{model_filename}' created in {os.getcwd()}")