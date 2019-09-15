largest = None
smallest = None
while True:
    num=input('Enter a number:')
    if num=='done':
        break
    try:
        val=float(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest=val
    elif val < smallest:
        smallest=val

    if largest is None:
        largest=val
    elif val > largest:
        largest=val

print("Minimum is ",smallest)
print("Maximum is ",largest)
