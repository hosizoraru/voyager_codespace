n = int(input())
if n == 0:
    print('除0错误，n不能等0')
    print('程序结束')
    exit()
sum = 0
for i in range(n):
    try:
        num = float(input())
    except:
        print('数值错误')
        print('程序结束')
        exit()
    else:
        sum += num
print('正确')
print('avg={:.2f}'.format(sum/n))
print('程序结束')