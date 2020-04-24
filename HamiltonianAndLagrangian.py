"""
You want to find all the marks that are not smaller than those on its right side in the array.
"""



N = int(input())
arr = list(map(int,input().split()))

aux = []
cur = arr[N-1]
aux.append(cur)
for i in range(N-2,-1,-1):
    if arr[i] >= cur:
        # print(arr[i],end=' ')
        cur = arr[i]
        aux.append(cur)

for i in range(len(aux)-1,-1,-1):
    print(aux[i],end=' ')
