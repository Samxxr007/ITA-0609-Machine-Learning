import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset
X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([0,0,0,1,1,1])

# Create Logistic Regression model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Test data
test = np.array([[2],[4],[5],[6]])

# Sigmoid probability
probability = model.predict_proba(test)[:,1]

# Classification
prediction = model.predict(test)

# Accuracy
accuracy = accuracy_score(y, model.predict(X))

print("Sigmoid Output:")
print(np.round(probability, 3))

print("Classification:")
print(prediction)

print("Accuracy:", accuracy * 100, "%")