a = input()
b = input()
la = len(a)
lb = len(b)
if (la == lb):
    if (a == b):
        print('all')
    else:
        print('no')
elif (la > lb):
    lc = la - lb
    if (a.find(b, lc) != -1):
        print(b)
    else:
        print('no')
elif (la < lb):
    lc = lb - la
    if (b.find(a, lc) != -1):
        print(a)
    else:
        print('no')
