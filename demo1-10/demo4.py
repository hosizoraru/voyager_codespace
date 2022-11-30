i = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
m = {}
while True:
    s = input().split()
    if s[0] == '#':
        break
    m[s[0]] = s[1]
    i[s[1]] += 1
print(m)
print(i)
for l in i.keys():
    print('等级{}: {}人'.format(l,i[l]))
    if i[l] >0:
        print('   分别是：  ',end='')
        for o in m.keys():
            if m[o] == l:
                print(o,end='  ')
        print()