def computepay(h,r):
    if h > 40:
        p = 40*r+(h-40)*r*1.5
        return (p)
    p = h*r
    return (p)
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print(p)
