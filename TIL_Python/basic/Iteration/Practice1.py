sum = 0
count = 0

while True:
    num = input("Enter a number:")
    try:
        num = int(num)
        if num != 'done':
            sum += num
            count += 1
            average = sum / count
            continue
        elif num == 'done':
            break
    except:
        if num != 'done':
            print("Invalid output")
            continue
        else:
            break

print(sum, count, average)

                

                
            



