def fun(l,r):
    global x
    if l>r:
        return 0
    if x[l]=='X':
        return fun(l+1,r)+1
    elif x[r]=='X':
        return fun(l,r-1)+1
    return 0
while True:
    n=int(input())
    if n==0:
        break
    l,m,ans=[],0,0
    for i in range(n):
        x=input()
        l.append(fun(0,len(x)-1))
        m=max(m,l[len(l)-1])
    for i in range(n):
        ans+=m-l.pop()
    print(ans)