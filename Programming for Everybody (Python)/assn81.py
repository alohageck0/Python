fname = raw_input("Enter file name: ")
fn = open(fname)
for line in fn:
    line = line.rstrip()
    print line.upper()