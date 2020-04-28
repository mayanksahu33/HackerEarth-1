"""
Given an array, A, of length N. Find the absolute difference between the smallest and largest prime number in array A.
"""

def SieveOfEratosthenes(low,up):
    if low == 1:
        low = 2
    prime = [True for i in range(up + 1)]

    p = 2
    while (p * p <= up):
        if (prime[p] == True):
            for i in range(p * 2, up + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    res = []
    for p in range(low,up +1):
        if prime[p]:
            res.append(p)
    return res

n = int(input())
arr = list(map(int,input().split()))
# possible = sieveOfAtkin(min(arr),max(arr))
possible = SieveOfEratosthenes(min(arr),max(arr))
# print(possible)
if possible:
    i = 0
    j = len(possible)-1
    min = possible[i]
    max = possible[j]
    find_max = False
    find_min = False

    while ( not (find_min and find_max) or i == j ):
        if possible[i] in arr:
            find_min = True
            min = possible[i]
        elif possible[i] not in arr:
            i += 1
        if possible[j] in arr:
            find_max = True
            max = possible[j]
        elif possible[j] not in arr:
            j -= 1

    if find_max and find_min:
        print(abs(max-min))
    else:
        print(1)
else:
    print(-1)




