largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if len(num) < 1 : break
    try :
        num = int(num)
        if smallest is None :
            smallest = num
            largest = num
        elif num < smallest :
            smallest = num
        elif num > largest :
            largest = num
    except : 
        print "Invalid input"
        break
print "Maximum is", largest
print "Minimum is", smallest