data = [1, 2, 3, 10, 11, 12]

# initial means
m1 = 2
m2 = 11

for iteration in range(5):
    c1 = []
    c2 = []
    
    # assignment step
    for x in data:
        if abs(x - m1) < abs(x - m2):
            c1.append(x)
        else:
            c2.append(x)
    
    # update step
    m1 = sum(c1) / len(c1)
    m2 = sum(c2) / len(c2)

    print("Iteration:", iteration+1)
    print("Cluster1:", c1)
    print("Cluster2:", c2)

print("Final Means:", m1, m2)