"""
Oz has a list arr[] of M integers. He has to find all integers K such that :

1) K > 1
2) arr[1]%K = arr[2]%K = arr[3]%K = ... = arr[M]%K where '%' is a modulus operator
"""


M = int(input())
arr = []
for i in range(M):
    arr.append(int(input()))
mikr = min(arr)
res = []
for i in range(2,mikr+1):
    tmp = arr[0] % i
    for j in range(1,M):
        if arr[j] % i != tmp:
            break
    if j == M-1:
        res.append(i)
for i in res:
    print(i,end=' ')



