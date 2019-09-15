s= None
print('Before')
for i in [9, 41, 12, 3, 74, 15]:
    if s is None:
        s=i
    elif i < s:
        s=i
    print(s, i)
print('After', "smallest:",s)
