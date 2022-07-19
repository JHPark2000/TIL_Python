# Get name of file and print how many lines that start with 'Subject' in it.
# If inputted name is "na na boo boo", print "NA NA BOO BOO TO YOU - You have been punk'd!"

print("Python egg.py")
fname = input("Enter the file name:")
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        data = open(fname)
        count = 0
        for line in data:
            if line.startswith('Subject:'):
                count += 1
        print("There were", count, "subject line in", fname)
    except:
        print("File cannnot be opened:", fname)

