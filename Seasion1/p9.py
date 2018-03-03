n=int(input())
odd=99999999990
s=0
for i in map(int,input().split()):
    if i%2==1:
        odd=min(odd,i)
    s+=i
print(s if s%2==0 else s-odd)