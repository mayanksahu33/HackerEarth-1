"""
Find and Print All The Prime Numbers Between L and R (Both L and R Inclusive)
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

L , R = list(map(int,input().split()))
# print(L,R)
for i in SieveOfEratosthenes(L,R):
    print(i,end=' ')

