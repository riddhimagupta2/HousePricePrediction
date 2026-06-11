import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

print("Loading dataset...")

# Load dataset
df = pd.read_csv("dataset/train.csv")

# Target column
y = df["SalePrice"]

# Features
X = df.drop("SalePrice", axis=1)

# Convert categorical columns to numeric
X = pd.get_dummies(X)

# Fill missing values
X = X.fillna(0)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")

# Save model and columns
joblib.dump(model, "house_price_model.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")

print("Model saved successfully!")
print("house_price_model.pkl created")
print("columns.pkl created")