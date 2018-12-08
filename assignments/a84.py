fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    listofwords = line.split()
    for word in listofwords:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
