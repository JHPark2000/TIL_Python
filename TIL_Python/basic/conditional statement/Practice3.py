# Write a code that receives a score between 0.0 and 1.0.
# If it is out of range, display an error message. Or if it is in range, use the table below to display your grade.

s = input("Enter score:")

try:
  s = float(s)
  if s>0.0 and s<1.0:
    if s>=0.9:
     print("A")
    elif s>=0.8:
     print("B")
    elif s>=0.7:
     print("C")
    elif s>=0.6:
     print("D")
    elif s<0.6:
     print("F")
  else:
    print("Bad score")
    
except:
  print("Bad score")
