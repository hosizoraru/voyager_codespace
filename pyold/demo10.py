code = []
name = []
scores = []
while True:
  s = input().split()
  if s == ['#']:
    break
  code.append(int(s[0]))
  name.append(str(s[1]))
  scores.append(int(s[2]) + int(s[3]) + int(s[4]))
new = scores.copy()
new.sort()
print(len(new))
for i in range(len(code)):
  n = scores.index(new[i])
  print('{}, {}, {}'.format(code[n],name[n],scores[n]))