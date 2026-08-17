import math

data = [
    [1,2,'A'],
    [2,3,'A'],
    [6,7,'B'],
    [7,8,'B']
]

test = [3,3]
k = 3

distances = []
for row in data:
    d = math.sqrt((row[0]-test[0])**2 + (row[1]-test[1])**2)
    distances.append((d, row[2]))

distances.sort()

neighbors = distances[:k]
votes = {}

for d,cls in neighbors:
    votes[cls] = votes.get(cls,0) + 1

prediction = max(votes, key=votes.get)
print("Predicted Class:", prediction)