f1, e1, f2, e2 = 65, 90, 97, 122
li = []
while True:
    try:
        x = input()
        l, r = 0, 0
        for i in range(len(x)):
            ch = ord(x[i])
            if ch >= f1 and ch <= e1 or ch >= f2 and ch <= e2:
                r = i + 1
            else:
                if l <= r and r != 0:
                    li.append(x[l:r].lower())
                l = i + 1
        if l <= r and r != 0:
            li.append(x[l:r].lower())
    except EOFError:
        break
print("\n".join(sorted(list(set(li)))))