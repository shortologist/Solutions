tu =('.', ',', '!', '?',' ')
x=''
def rEc(i,j):
    if i>=j:
        return True
    if x[i]==x[j] or (x[i] in tu and x[j] in tu):
        return rEc(i+1,j-1)
    elif x[i] in tu:
        return rEc(i+1,j)
    elif x[j] in tu:
        return rEc(i,j-1)
    return False
while True:
    x=input().lower()
    if x=='done':
        break
    print("You won't be eaten!"if rEc(0,len(x)-1) else 'Uh oh..')