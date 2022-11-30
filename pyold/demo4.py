s = input()
n = int(input())
c = input()
for i in range(len(s)) :
  if s[i] == c :
    n -= 1
  if n == 0 :
    print(i + 1)
    break
if n != 0 :
  print('no')