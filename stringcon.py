sval='123'
eval=type(sval)
print(eval)
ival=int(sval)
dval=type(ival)
print(dval)
print(ival+1)
try:
    nsv=('Hello Sourav')
    niv=int(nsv)
except:
    print('string should be in numeriacal value to perform type conversion:',nsv)
