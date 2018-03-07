while True:
    try:
        x=input()[::-1]
        x=x.split()
        print(' '.join(x[::-1]))
    except EOFError:
        break