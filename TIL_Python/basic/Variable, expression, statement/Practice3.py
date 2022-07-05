#Make the program gets time for caculating pay and cost per time
#Be sure to input data as... Hours = 35, Rate = 2.75, round = 2

# 3 ways to solve it

# No.1
Hours = input("Enter Hours:")
Rate = input("Enter rate:")
pay = round(float(Hours) * float(Rate),2)
print(pay)

# No.2
Hours = input("Enter Hours:")
Rate = input("Enter rate:")
print("Pay: %.2f"%(Hours * Rate))

# No.3
Hours = float(input("Enter Hours:"))
Rate = float(input("Enter rate:"))
print(round(Hours*Rate,2))
