fname = raw_input("Enter file name: ")
fn = open(fname)
#fn = open('romeo.txt')
romeo = []
words = []
for line in fn:
    line = line.rstrip()
    line = line.split()
    romeo.append(line)
for array in romeo:
    for word in array:
        if word not in words:
            words.append(word)
words.sort()
print words
