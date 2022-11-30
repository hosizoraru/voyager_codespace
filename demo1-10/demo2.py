dicAreas = {'Russia':1707.5,'Canada':997.1,'China':960.1}
IsVK = [(v,k) for k,v in dicAreas.items()]
IsVK.sort()
IsVK = [(k,v) for v,k in IsVK]
print(IsVK)