#initialize vars
n = 0
minnum = None
maxnum = 0
while True:
    s = input('enter number: ')
    if s == 'done':
        break
    try:
        i = int(s)
    except:
        print('Invalid input')
    for j in [i]:
        if j > maxnum :
            maxnum = j
        elif minnum is None:
            minnum = j
        elif j < minnum :
            minnum = j
print('Maximum is',maxnum)
print('Minimum is', minnum)
