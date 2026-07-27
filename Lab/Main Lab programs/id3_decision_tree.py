data = [
['Sunny','No'],
['Rainy','Yes'],
['Sunny','No']
]

tree = {}
for row in data:
    key = row[0]
    tree[key] = row[1]

print("Decision Tree:", tree)