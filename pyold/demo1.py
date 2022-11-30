def printpy(x):
    ax = 2 * x - 1
    for i in range(1, x+1):
        str = ''
        bx = 2 * i - 1
        cx = (ax - bx) // 2
        for j in range(0, cx):
            str += ' '
        for j in range(0, bx):
            str += '*'
        for j in range(0, cx):
            str += ' '
        print(str)


x = eval(input())
printpy(x)
