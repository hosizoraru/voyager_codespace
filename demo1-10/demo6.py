a = eval(input())
b = eval(input())
for i in a.keys():
    for l in b.keys():
        if i == l:
            a[i] += b[l]
b.update(a)
c = [(q,w) for w,q in b.items()]
c.sort(reverse=True)
for m in range(len(c)):
    d = c[m]
    print('{}销量{}'.format(d[1],d[0]))