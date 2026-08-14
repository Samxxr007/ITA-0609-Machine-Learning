import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataset
X = np.array([[1,2],[2,3],[3,4],
              [6,7],[7,8],[8,9]])

y = np.array(['A','A','A','B','B','B'])

# Input K
k = int(input("Enter K: "))

# Create KNN model
model = KNeighborsClassifier(n_neighbors=k,
                             metric='euclidean')

# Train model
model.fit(X, y)

# Test data
test = np.array([[4,5]])

# Prediction
prediction = model.predict(test)

# Training accuracy
predicted = model.predict(X)
accuracy = accuracy_score(y, predicted)

print("Test Data:", test)
print("Predicted Class:", prediction[0])
print("Accuracy:", accuracy * 100, "%")