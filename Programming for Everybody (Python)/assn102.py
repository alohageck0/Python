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
time = []
for str in from_:
    str = str.split()
    from_split.append(str)
for item in from_split:
    time.append(item[5])
time_split = []
for hour in time:
    hour = hour.split(':')
    time_split.append(hour)
hours_only = []
for x in time_split:
    hours_only.append(x[0])
d = dict()
for email in hours_only:
    d[email] = d.get(email,0)+1
sor = d.items()
sor.sort()
for k,v in sor:
    print k, v