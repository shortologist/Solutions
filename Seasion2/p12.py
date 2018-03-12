while True:
    n=int(input())
    if n==0:
        break
    l=[0 for i in range(n)]
    for i in range(n):
        s=0
        li=list(map(int,input().split()))
        for j in range(n):
            l[j]+=li[j]
            s+=li[j]
        l.append(s)
    x,y,te=-1,-1,False
    for i in range(n):
        if l[i]%2==1:
            if x!=-1:
                te=True
                break
            else:
                x=i+1
    if not te:
        for i in range(n,2*n):
            if l[i]%2==1:
                if x==-1 or y!=-1:
                    te=True
                    break
                else:
                    y=i+1
    if te:
        print('Corrupt')
    elif x+y==-2:
        print('OK')
    else:
        print('Change bit (',y-n,',',x,')',sep='')