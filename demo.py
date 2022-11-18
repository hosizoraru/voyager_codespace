s = input()
month = int(s[4:6])
if month in [1,2,3]:
    print('spring')
elif month in [4,5,6]:
    print('summer')
elif month in [7,8,9]:
    print('autumn')
elif month in [10,11,12]:
    print('winter')