# Get file nam and read it
# Find lines like below type : starts with 'X-DSPAM-Confidence:'
# If you find it, Get sum value of numbers is in right sides of ':'

fname = input("Enter the file name:")
sum = None
count = 0

for line in open(fname):
    if line.startswith("X-DSPAM-Confidence:"):
        point = line.find(":")+1

        if sum == None:
            sum = float(line[point : len(line)])
        else:
            sum = sum + float(line[point : len(line)])
        count += 1

print("Average spam confidence:", sum/count)
    
        

