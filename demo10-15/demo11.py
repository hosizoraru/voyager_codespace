def isPrime(num):
    try:
        intnum = int(num)
    except:
        return False
    

num = input()
if isPrime(num):
    print('yes')
else:
    print('no')