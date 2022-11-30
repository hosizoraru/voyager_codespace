n = int(input())
a = 0
b = 0
for i in range(n):
    s = input().split()
    if s == 'null':
        break
    if s[0] > s[1]:
        a += 1
    elif s[0] < s[1]:
        b += 1
if a == b:
    print("CONTINUE")
elif a > b:
    print("Sg")
elif a < b:
    print("Gs")
