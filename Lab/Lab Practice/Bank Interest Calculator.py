p = float(input("Principal: "))
r = float(input("Rate (%): "))
t = float(input("Time (years): "))

si = (p * r * t) / 100
ci = p * ((1 + r/100) ** t - 1)

print("Simple Interest:", si, "Compound Interest:", ci)
