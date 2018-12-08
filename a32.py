hrs = input("enter hours: ")
rate = input("enter rate: ")
hrs = float(hrs)
rate = float(rate)
if hrs == 40:
    pay=hrs*rate
if hrs < 40:
    pay=hrs*rate
if hrs > 40 :
    pay = (hrs-40)*rate*1.5+40*rate
print(pay)
