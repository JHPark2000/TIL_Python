#Reading files and convering it as capital by a line
#Testing file is in "https://www.py4e.com/code3/mbox-short.txt"

fname = input("Enter a file name:")
for line in open(fname):
    line = line.upper()
    print(line)


