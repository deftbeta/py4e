fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    valtext = line[19:]
    val = float(valtext)
    count = count + 1
    total = total + val
    print('i: ', count, 'val: ', val,'sum:',total)
average = total/count
print('average =',average)
print("Done")
