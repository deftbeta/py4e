import re
name = input('enter file name ')
fh = open(name)
numlist = list()
sum = 0
sumlen = 0
count =0
for line in fh:
    line = line.strip()
    valstoadd = re.findall('[0-9]+',line)
    #print(valstoadd)
    if len(valstoadd) < 1: continue
    lenx = len(valstoadd)
    sumlen = sumlen + lenx
    #print(lenx)
    #print(sumlen)
    #print(valstoadd)
    for val in valstoadd:
        floatval = float(val)
        sum = sum + floatval
        #print(sum)
    #num = float(valstoadd[0])
    #print(num)
    #count = count +1
    #sum = num + sum
    #print('count: ', count)
    #print('sum: ', sum)
    #numlist.append(num)
    #numlist.append(valstoadd)
#print('list of nums: ',numlist)
#print('total sum: ', sum)
print(sum)
