import numpy as np
from sklearn.ensemble import IsolationForest

# Load your dataset
data = np.loadtxt('network_traffic_data.csv', delimiter=',')

# Train the model
model = IsolationForest(n_estimators=100, contamination=0.1)
model.fit(data)

# Predict anomalies
anomalies = model.predict(data)
