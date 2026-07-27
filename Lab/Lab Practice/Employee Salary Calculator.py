basic = float(input("Enter basic salary: "))
pf = basic * 0.12
tax = basic * 0.10
net = basic - (pf + tax)

print("Gross:", basic, "PF:", pf, "Tax:", tax, "Net:", net)
