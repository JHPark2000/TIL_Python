# Make pay-calculating program again. Even if a non-numeric value is entered, the program must be safely terminated.

H = float(Hours)
R = float(Rate)

try :
  if H<40:
    pay = h * r
    print(pay)
  else:
    pay = r * (1.5 * h -20) 
    print(pay)
    
except:
  print("Error, please enter numeric input")
