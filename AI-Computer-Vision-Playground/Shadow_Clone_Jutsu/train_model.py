import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# 1. Load data
data = pd.read_csv("jutsu_data.csv", header=None)

# 2. Split features (X) and labels (y)
# The first 126 columns are hand landmark points (X), the last column is the label (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 3. Split into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model (Random Forest works well for this jutsu detection task)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 5. Evaluate accuracy
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {score * 100:.2f}%")

# 6. Save the model for later use
with open("jutsu_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Done! The model has been trained and saved as 'jutsu_model.pkl'.")
