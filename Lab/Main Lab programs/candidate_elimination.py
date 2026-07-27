S = ['0','0','0','0','0','0']
G = ['?','?','?','?','?','?']

data = [
['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
['Rainy','Cold','High','Strong','Warm','Change','No']
]

for row in data:
    if row[-1] == 'Yes':
        for i in range(len(S)):
            if S[i] == '0':
                S[i] = row[i]
            elif S[i] != row[i]:
                S[i] = '?'
    else:
        for i in range(len(G)):
            if G[i] == '?':
                G[i] = row[i]

print("S:", S)
print("G:", G)