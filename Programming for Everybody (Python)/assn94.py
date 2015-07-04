name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
temp = []
y = []
for line in fh:
    line = line.rstrip()
    temp.append(line)
from_ = []
for line_ in temp:
    if line_.startswith('From '):
        from_.append(line_)
        
from_split = []
for str in from_:
    str = str.split()
    from_split.append(str)
emails = []
for item in from_split:
    emails.append(item[1])
d = dict()
for email in emails:
    d[email] = d.get(email,0)+1
bigitem = None
bigcount = None
for email,count in d.items():
    if bigitem == None or count > bigcount:
        bigitem = email
        bigcount = count
print bigitem, bigcount    

