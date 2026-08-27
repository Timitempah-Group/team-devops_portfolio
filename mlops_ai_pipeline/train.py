import joblib
import json
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Loading Iris dataset...")
data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training RandomForestClassifier...")
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Test accuracy: {accuracy:.4f}")

os.makedirs("outputs", exist_ok=True)
joblib.dump(model, "outputs/model.pkl")

metrics = {"accuracy": accuracy, "n_estimators": 50, "test_size": 0.2}
with open("outputs/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("Model and metrics saved to outputs/")
