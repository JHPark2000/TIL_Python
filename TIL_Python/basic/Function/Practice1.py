def computepay(hours, rate):
  if hours > 40:
    result = (hours -40) * rate * 1.5 + 40 * rate
    return result
  else:
    result = hours * rate
    return result

a = float(input("Enter Hours:"))
b = float(input("Enter Rate:"))
c = computepay(a,b)
print("Pay:", c)
