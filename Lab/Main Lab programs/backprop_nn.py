import numpy as np

# input and target
X = np.array([[0,1],[1,1]])
y = np.array([[0],[1]])

# weights
w = np.random.rand(2,1)

# sigmoid
def sig(x):
    return 1/(1+np.exp(-x))

# training
for i in range(1000):
    out = sig(np.dot(X, w))
    err = y - out
    w += np.dot(X.T, err * out * (1 - out))

print("Output:", out)