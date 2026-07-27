food = float(input("Enter food cost: "))
gst = food * 0.05
service = food * 0.1
total = food + gst + service

print("GST:", gst, "Service:", service, "Total Bill:", total)
