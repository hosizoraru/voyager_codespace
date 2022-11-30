for i in range(1, 4):
    for j in range(1, 4):
        print("%3d" % (i*j), end='')
        if j % 2 == 0:
            break
    if j == 4:
        break
print()
