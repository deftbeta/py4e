import re
name = input('enter file name ')
fh = open(name)
numlist = list()
sum = 0
for line in fh:
    line = line.strip()
    valstoadd = re.findall('[0-9]+',line)
    if len(valstoadd) < 1: continue
    for val in valstoadd:
        floatval = float(val)
        sum = sum + floatval
print(sum)
