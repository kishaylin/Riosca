import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

# Load the Irish Stock Exchange dataset
df = pd.read_csv("irish_stock_exchange_companies.csv")

# Features and Target
X = df.drop(columns=["company_id", "risk_label"])
y = df["risk_label"]

# Train model
model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X, y)

# Save updated model
joblib.dump(model, "company_risk_model.pkl")
print("Model successfully retrained on Irish Stock Exchange companies!")