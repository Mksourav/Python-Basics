def computepay(h,r):
    try:
        h=float(h)
        r=float(r)
    except:
        print('Error! The value should be in numerical form!')
    if h>40:
        cp=(h*(1.5*r)-(40*(0.5*r)))
        return cp
    else:
        if h>0:
            cp=h*r
            return cp
        else:
            print('Error! The value should be greater than zero!')

h=input('Enter the Hours:')
r=input('Enter the Rate per hours:')
p = computepay(h,r)
print("Pay",p)
