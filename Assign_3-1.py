hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error! Please enter the numeric value")
    quit()
print(h, r)
if h>40:
    eh = h-40 #eh= extra hour
    nh = h-eh #nh= normal hour
    xp = ((nh*r)+(eh*(r*1.5)))
    print("Pay:",xp)
else:
    xp = h * r
    print("Pay:",xp)
