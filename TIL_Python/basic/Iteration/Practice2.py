max = None
min = None

while True:
    num = input("Enter a number:")
    try: 
        if num != 'done':
            num = int(num)
            if max == None and min == None:
                max = num
                min = num
                continue
            else:
                if max < num:
                    max = num
                    continue
                else:
                    if min > num:
                        min = num
                        continue
                    else:
                        continue
        elif num == 'done':
            break
    except:
        if num != 'done':
            print("Invalid output")
            continue
        else:
            break

print(max, min)
