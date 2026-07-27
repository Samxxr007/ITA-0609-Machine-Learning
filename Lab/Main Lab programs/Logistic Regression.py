import math

X = [1, 2, 3, 4]
Y = [0, 0, 1, 1]

w = 0.0
b = 0.0
lr = 0.1

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# training loop
for epoch in range(200):
    for i in range(len(X)):
        z = w * X[i] + b
        y_pred = sigmoid(z)
        
        error = Y[i] - y_pred
        
        # update weights
        w = w + lr * error * X[i]
        b = b + lr * error

print("Final weight:", w)
print("Final bias:", b)

# prediction
test = 3
z = w * test + b
pred = sigmoid(z)

print("Predicted value:", pred)
print("Class:", round(pred))