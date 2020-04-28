"""
You have given two integer L,R. A ultra prime number is a prime number whose sum of digit is also prime. Now you have to count all such ultra prime number in range [L,R] .
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
            


def isPrime(n) : 
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while(i * i <= n) : 
        if n % i == 0 or n % (i + 2) == 0 : 
            return False
        i = i + 6
    return True 

from sys import stdin,stdout

T = int(input())
for _ in range(T):
    l , u = list(map(int,stdin.readline().split()))

    possible = SieveOfEratosthenes(l,u)
    # print(possible)
    cnt = 0
    for i in possible:
        res = [int(x) for x in str(i)]
        if isPrime(sum(res)):
            cnt +=1
    stdout.write(str(cnt)+'\n')

