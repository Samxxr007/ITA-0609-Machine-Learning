balance = 5000
pin = 1234
entered_pin = int(input("Enter PIN: "))
if entered_pin == pin:
    amt = int(input("Enter amount: "))
    if amt <= balance:
        balance -= amt
        print("Withdrawal successful. Balance:", balance)
    else:
        print("Insufficient balance.")
else:
    print("Invalid PIN.")
