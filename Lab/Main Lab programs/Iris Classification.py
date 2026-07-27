import math

# [sepal length, petal length, class]
data = [
    [5.1, 1.4, 'Setosa'],
    [6.0, 4.5, 'Versicolor'],
    [6.5, 5.5, 'Virginica']
]

test = [5.0, 1.5]

distances = []

for row in data:
    d = math.sqrt((row[0] - test[0])**2 + (row[1] - test[1])**2)
    distances.append([d, row[2]])

# sort
distances.sort(key=lambda x: x[0])

# nearest neighbor
nearest = distances[0]

print("Distances:", distances)
print("Nearest:", nearest)
print("Predicted Class:", nearest[1])