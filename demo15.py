try:
    n = int(input())
except:
    print('输入的人数必须是数字,大于0并且小于等于100')
    exit()
else:
    if n <= 1 or n > 100:
        print('输入的人数必须是数字,大于0并且小于等于100')
        exit()
stu = {}
yuwenc = []
for i in range(n):
    s = input().split()
    name = s[0] + ' ' + s[1] + ' ' + s[2] + ' ' + s[3] + ' ' + s[4] +' '
    sum = int(s[2]) + int(s[3]) + int(s[4])
    yuwenc.append(int(s[2]))
    avg = '{:.2f}'.format(sum/3)
    stu[name] = avg
    
stuc= [(m,n) for (n,m) in stu.items()]
stuc.sort(reverse=True)
for (m,n) in stuc:
    print('{}{}'.format(n,m))