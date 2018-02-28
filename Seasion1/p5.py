input()
l=[0 for i in range(26)]
c=0
for i in input():
    if l[ord(i.lower())-ord('a')]==0:
        l[ord(i.lower()) - ord('a')] =1
        c+=1
if c==26:
    print('YES')
else:
    print('NO')