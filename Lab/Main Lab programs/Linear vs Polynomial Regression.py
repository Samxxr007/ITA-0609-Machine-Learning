X = [1, 2, 3, 4]
Y = [1, 4, 9, 16]

# linear model
m = sum(X[i]*Y[i] for i in range(4)) / sum(x*x for x in X)
linear_preds = []

for x in X:
    linear_preds.append(m * x)

# polynomial model (degree 2)
poly_preds = []
for x in X:
    poly_preds.append(x * x)

# calculate squared error
linear_error = 0
poly_error = 0

for i in range(len(X)):
    linear_error += (Y[i] - linear_preds[i]) ** 2
    poly_error += (Y[i] - poly_preds[i]) ** 2

print("Linear Predictions:", linear_preds)
print("Polynomial Predictions:", poly_preds)

print("Linear Error:", linear_error)
print("Polynomial Error:", poly_error)