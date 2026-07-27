# dataset: [feature, class]
data = [
    ['Sunny', 'Yes'],
    ['Sunny', 'Yes'],
    ['Rainy', 'No'],
    ['Rainy', 'No']
]

test = 'Sunny'
classes = ['Yes', 'No']

probabilities = {}

# compute prior and likelihood
for c in classes:
    subset = [row for row in data if row[1] == c]
    
    # prior
    prior = len(subset) / len(data)
    
    # likelihood
    count = 0
    for row in subset:
        if row[0] == test:
            count += 1
    
    likelihood = count / len(subset)
    
    # posterior
    probabilities[c] = prior * likelihood

print("Class Probabilities:", probabilities)
prediction = max(probabilities, key=probabilities.get)
print("Predicted Class:", prediction)