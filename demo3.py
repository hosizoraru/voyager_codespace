student = eval(input())
max = 0
for i in student.keys():
    s = student[i]
    sum = 0
    for l in s.keys():
        sum += s[l]
        if sum > max:
            max = sum
            p = i
print('总分最高的是{}{}分'.format(p,max))
