from math import log2
x=int(input())
c=0
while x!=0:
    x-=2**int(log2(x))
    c+=1
print(c)