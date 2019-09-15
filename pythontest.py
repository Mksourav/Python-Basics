#PLAY WITH PYTHON
print("-------Hello Sourav, Welcome to python-------")
x=5
if x<2:
    print('Below 2')
elif x>=2:
    print('Two or more')
else:
    print("Something else")

eee='hello' + ' there'
fff=58
eee=eee
print(eee)
d=type(eee)
print(d)
e=type(fff)
print(e)
print(float(99)+100)
i=42
j=type(i)
print(j)
f=float(i)
print(f)
f=type(f)
print(f)
print(10/2)
print(9/2)
print(99/100)
print(10.0*2.0)
sval='123'
t=type(sval)
print(t)
ival=int(sval)
t=type(ival)
print(t)
print(ival+1)
name=input('who are you?')
print('welcome',name)
inp=input('Europe floor?')
usf=int(inp)+1
print('US floor', usf)
print("123"+"abc")
x = 1 + 2 * 3 - 8 / 4
print(x)
x=int(98.6)
print(x)

#Get the name of the file and open it
name=input('Enter file:')
handle=open(name, 'r')

#count word frequency
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

#Find the most common word
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count

# All done
print(bigword, bigcount)
