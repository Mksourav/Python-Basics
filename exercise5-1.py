n=0
s=0
while True:
    d=input('Enter the value:')
    if d=='done':
        break
    try:
        val=float(d)
    except:
        print('Invalid input!')
        continue
    n=n+1
    s=s+val
print(s, n, s/n)
