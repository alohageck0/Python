score = raw_input("Enter score between 0.0 and 1.0:")
try:
	s = float(score)
except:
	print "invalid score"
	quit()
#print s
if s>1.0:
	print "Score >1.0"	
elif s>=0.9:
	print "A"
elif s>=0.8:
	print "B"
elif s>=0.7:
	print "C"
elif s>=0.6:
	print "D"
elif s<0.0:
	print "Score <0.0"
else:
	print "F"