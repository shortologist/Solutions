s1=input()
s2=input()
for i in range(len(s1)):
    if s1[i].lower()>s2[i].lower():
        print(1)
        exit()
    elif s1[i].lower()<s2[i].lower():
        print(-1)
        exit()
print(0)