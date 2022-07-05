# Calculate that workers who have worked more than 40 hours are paid 1.5 times the hourly wage.

Hours = input("Enter Hours:")
Rate = input("Enter Rate:")

h = float(Hours)
r = float(Rate)

if h<40:
  pay = h * r
  print(pay)
else:
  pay = r * (1.5 * h -20) 
  print(pay)
