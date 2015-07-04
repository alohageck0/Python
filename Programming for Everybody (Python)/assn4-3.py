
def computepay(h,r):   
    h = int(h)
    r = float(r)
    if h<=40:
	    p = h*r
    else:
	    p = 40*r+(h-40)*1.5*r
    return p
hours = raw_input("Enter hours:")
rate = raw_input("Enter rate:")
pay = computepay(hours,rate)
print "Pay",pay