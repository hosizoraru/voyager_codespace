def rabit(n):
    if n <= 0:
        return 0
    elif 0 < n <= 2:
        return 1
    elif n >= 3:
        return rabit(n-1) + rabit(n-2)

n = int(input())
print(rabit(n))
