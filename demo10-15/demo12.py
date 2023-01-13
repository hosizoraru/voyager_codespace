fo = open('result.txt','r+')
text = fo.read()
text = text.split('，')
textc = {}
for i in text:
    textc[i] = textc.get(i,0) + 1
texti = [(m,n) for (n,m) in textc.items()]
texti.sort()
for (m,n) in texti:
    print('{}:{}'.format(n,m))
fo.close()
fo2 = open('result.txt','a')
fo2.write('\n')
for (m,n) in texti:
    fo2.write('{}:{} '.format(n,m))
fo2.close()
