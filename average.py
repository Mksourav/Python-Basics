c=0 # For count
s=0 # For sum
print('Before'," count:",c," sum:",s)
for i in [9, 41, 12, 3, 74, 15]: # i for iteration
    c=c+1
    s=s+i
    print(c, s, i)
print('After'," count:",c," sum:",s," Average:",s/c)
