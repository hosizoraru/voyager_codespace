n = int(input())
sum = 0
for i in range(n):
    s = input()
    sc = s.split()
    try:
        sum += float(sc[0])
    except:
        print('Error for data "{}"! Break'.format(s))
        print('Process Completed')
        exit()
print('All OK')
print('avg grade = {:.2f}'.format(sum/n))
print('Process Completed')