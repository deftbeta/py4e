fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From:") : continue
    line = line.rstrip()
    line = line.split()
    emails = line[1]
    count = count + 1
    #print(email,", ",count)
    print(emails)

#if len(fname) < 1 : fname = "mbox-short.txt"
print("There were", count, "lines in the file with From as the first word")
