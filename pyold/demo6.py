N = int(input())
for i in range(N):
    s = input()
    year = s[0:4]
    month = s[5:7]
    day = s[8:]
    if int(day) == 1:
        if int(month) in [3]:  # 2
            month = str(int(month) - 1)
            if int(year) % 400 == 0:
                day = '29'
            elif int(year) / 4 == 0 and int(year) % 100 != 0:
                day = '29'
            else:
                day = '28'
        elif int(month) in [1]:  # 12
            year = str(int(year) - 1)
            day = '31'
        elif int(month) in [2, 4, 6, 8, 9]:  # 1 3 5 7 8
            month = str(int(month) - 1)
            day = '31'
        elif int(month) in [5, 7, 10, 11, 12]:  # 4 6 9
            month = str(int(month) - 1)
            day = '30'
    elif int(day) != 1:
        day = str(int(day) - 1)
    print('{}-{:0>2}-{:0>2}'.format(year, month, day))
