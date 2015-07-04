fname = raw_input("Enter file name: ")
fn = open(fname)
count = 0
total = 0
for line in fn:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line.rstrip()
    pos = line.find('0')
    num = line[pos:]
    fnum = float(num)
    total = total + fnum
    #print fnum
    #print total
    count = count + 1
print 'Average spam confidence:', total/count