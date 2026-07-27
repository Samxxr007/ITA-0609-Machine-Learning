X = [1, 2, 3, 4]
Y = [2, 4, 6, 8]

n = len(X)

# mean calculation
sum_x = sum(X)
sum_y = sum(Y)

mean_x = sum_x / n
mean_y = sum_y / n

# calculate slope
num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den

# intercept
c = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (c):", c)

# prediction
x_test = 5
y_pred = m * x_test + c

print("Predicted value:", y_pred)