scores = []
while True:
  s = input().split()
  if s == ['#']:
    break
  sum = int(s[2]) + int(s[3]) + int(s[4])
  s[2] = str(sum)
  del(s[3])
  del(s[3])
  scores.append(s)
scores.sort(key = lambda X:X[2],reverse= False)
print(scores)
for i in range(len(scores)):
  s = str(scores[i]).split()
  a = s[0].strip("'['']'")
  b = s[1].strip("'['']'")
  c = s[2].strip("'['']'")
  print('{}, {}, {}'.format(a[:len(a)-2:],b[:len(b)-2:],c[:len(c):]))