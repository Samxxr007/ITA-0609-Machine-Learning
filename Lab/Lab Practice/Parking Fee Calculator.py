hours = int(input("Enter parking hours: "))
vehicle = input("Enter vehicle type (Car/Bike): ")

rate = 20 if vehicle.lower() == "bike" else 50
fee = hours * rate

print("Parking Fee:", fee)
