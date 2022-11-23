def binarySearch (arr,l,r,x):
    if int(r) >= 1:
        mid = int(l+(r-1)/2)
        if int(arr[mid]) == x:
            return mid
        elif int(arr[mid]) > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1
arr = []
arr = input().split(',')
print(arr)
x = int(input())
if binarySearch(arr, 0, len(arr)-1, x) != -1:
    print(binarySearch(arr, 0, len(arr)-1, x))
else:
    print('no in arr')