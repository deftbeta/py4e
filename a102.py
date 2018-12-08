fname = input("Enter file:")
#emaildatelist = list()
counts = {}
fh = open(fname)
for line in fh:
    if not line.startswith("From") : continue
    line = line.rstrip()
    line = line.split()
    emaildate = line[5:6]
    #emaildatelist.append(emaildate)
    for datetimes in emaildate:
        if not datetimes.find(":") : continue
        splitdatetime = datetimes.split(':')
        emailhour = splitdatetime[0]
        #print(emailhour)
        counts[emailhour] = counts.get(emailhour, 0) +1
lst = []
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)
    lst = sorted(lst)
for key, val in lst[:]:
    print(key,val)
