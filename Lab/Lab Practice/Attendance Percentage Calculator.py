classes_held = int(input("Enter total classes held: "))
classes_attended = int(input("Enter classes attended: "))

percentage = (classes_attended / classes_held) * 100
status = "Eligible" if percentage >= 75 else "Not Eligible"

print("Attendance %:", percentage, "Status:", status)
