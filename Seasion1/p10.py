x=input()
m=('.',',','?','!')
for i in range(len(x)-1):
    if x[i] in m and x[i + 1] != ' ':
        print(x[i] + ' ', end='')
    elif not(x[i]==' ' and x[i+1]==' ' or x[i]==' ' and x[i+1] in m):
        print(x[i],end='')
print(x[len(x)-1])