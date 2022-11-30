def isPrime(num):
  try:
    n = int(num)
  except:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

num = input()
if isPrime(num):
    print('yes')
else:
    print('no')
