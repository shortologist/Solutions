while True:
    b,n=map(int,input().split())
    if b+n==0:
        break
    a=[int(i) for i in input().split()]
    for i in range(n):
        x,y,z=map(int,input().split())
        a[x-1]-=z
        a[y-1]+=z
    if min(a)<0:
        print('N')
    else:
        print('S')