import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data\expenses.csv")

# Prepare data
X = np.arange(len(df)).reshape(-1,1)
y = df["Amount"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next expense
next_day = [[len(df)]]
prediction = model.predict(next_day)

print("Predicted next expense:", prediction[0])