xyz1 = input()

tokens = xyz1.split()

a=int(tokens[0])
b=int(tokens[1])
c=[]
d=[]

i=1
while i<int(a+1):
    if (a%i)==0:
        c.append(i)
    i=i+1

j=1
while j<int(b+1):
    if (b%j)==0:
        d.append(j)
    j=j+1


