N = int(input())
if N == 3:
  for i in range(100,999):
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    num = a ** 3 + b ** 3 + c ** 3
    if num == i:
      print(i)
if N == 4:
  for i in range(1000, 9999):
    d = i // 1000
    a = (i - d * 1000) // 100
    b = (i - d * 1000 - a * 100) // 10
    c = (i - d * 1000 - a * 100 - b * 10) // 1
    num = a ** 4 + b ** 4 + c ** 4 + d ** 4
    if num == i:
      print(i)
if N == 5:
  for i in range(10000, 99999):
    e = i // 10000
    d = (i - e * 10000) // 1000
    a = (i - e * 10000 - d * 1000) // 100
    b = (i - e * 10000 - d * 1000 - a * 100 ) // 10
    c = (i - e * 10000 - d * 1000 - a * 100 - b * 10) // 1
    num = a ** 5 + b ** 5 + c ** 5 + d ** 5 + e ** 5
    if num == i:
      print(i)
