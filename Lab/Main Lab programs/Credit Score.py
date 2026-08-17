# dataset: [income, debt, class]
data = [
    [50000, 10000, 'Good'],
    [20000, 15000, 'Bad'],
    [60000, 5000, 'Good']
]

income = 40000
debt = 12000

# simple decision tree logic
if income > 45000:
    if debt < 10000:
        result = "Good"
    else:
        result = "Average"
else:
    if debt < 10000:
        result = "Average"
    else:
        result = "Bad"

print("Income:", income)
print("Debt:", debt)
print("Credit Status:", result)