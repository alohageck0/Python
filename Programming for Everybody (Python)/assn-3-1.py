hours = raw_input("Enter hours:")
rate = raw_input("Enter rate:")
h = int(hours)
r = float(rate)
if h<=40:
	print h*r
else:
	print 40*r+(h-40)*1.5*r
