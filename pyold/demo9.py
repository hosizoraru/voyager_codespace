s = input().split()
a = int(s[0])
n = int(s[1])
sum = 0
for i in range(2,n+2,2):
  num = int(str(a)*i)
  sum += num
print(sum)