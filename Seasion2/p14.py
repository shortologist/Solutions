while True:
    n=int(input())
    if n==0:
        break
    l=list(range(1,n+1))
    print('Discarded cards:',end='')
    if len(l)!=1:
        print(end=' ')
    while len(l)!=1:
        if len(l)!=2:
            print(l[0],end=', ')
        else:
            print(l[0],end='')
        del l[0]
        l.append(l[0])
        del l[0]
    print('\nRemaining card:',l[0])