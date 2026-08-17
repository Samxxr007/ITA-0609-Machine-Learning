X = [2015, 2016, 2017, 2018, 2019]
Y = [300000, 320000, 350000, 400000, 450000]

n = len(X)

mean_x = sum(X) / n
mean_y = sum(Y) / n

num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den
c = mean_y - m * mean_x

print("Model: y =", m, "x +", c)

# prediction
year = 2022
price = m * year + c

print("Predicted Price for", year, ":", int(price))