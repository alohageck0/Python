fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
temp = []
y = []
for line in fh:
    line = line.rstrip()
    temp.append(line)
from_ = []
for line_ in temp:
    if line_.startswith('From '):
        from_.append(line_)
        count = count + 1
for x in from_:
    x = x.split()
    y.append(x)
for array in y:
    print array[1]

print "There were", count, "lines in the file with From as the first word"
