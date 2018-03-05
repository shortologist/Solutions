n=int(input())
d={'M':1,'A':3,'R':2,'G':1,'I':1,'T':1}
while n!=0:
    ans=600
    a = {'M': 0, 'A': 0, 'R': 0, 'G': 0, 'I': 0, 'T':0}
    for i in input():
        if i in a.keys():
            a[i]+=1
    for i in a.keys():
        ans=min(ans,int(a[i]//d[i]))
    print(ans)
    n-=1