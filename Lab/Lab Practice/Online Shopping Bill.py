amount = float(input("Enter purchase amount: "))
discount = amount * 0.1
gst = (amount - discount) * 0.18
total = amount - discount + gst

print("Discount:", discount, "GST:", gst, "Total Bill:", total)
