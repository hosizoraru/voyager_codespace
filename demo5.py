n = int(input())
a,b,flag = 0,0,0
for i in range(n):
    test = {}
    flag = 0
    s = input().split()
    for c in s:
        test[c] = test.get(c,0) + 1
    for p in test.keys():
        if test[p] > 1:
            flag = 1
            break
    if flag == 0:
        a += 1
    else:
        b += 1
print('True={}, False={}'.format(b,a))
