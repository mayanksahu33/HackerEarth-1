"""
Given a number N find the smallest number K such that it satisfies all the 3 rules -
i) K >= N .
ii) K is a prime number
iii) K ≡ 1 (mod 11 )

"""

def SpecialSieveOfEratosthenes(low,up):
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
        if prime[p] and p % 11 == 1:
            res.append(p)
    return res

primes = SpecialSieveOfEratosthenes(2,pow(10,6)+100)

from bisect import bisect
from sys import stdin, stdout

N = int(input())
for _ in range(N):
    n = int(stdin.readline()) #for fast input
    pos = bisect(primes,n)

    if (primes[pos-1] == n):
        stdout.write(str(n)+'\n')
    else:
        stdout.write(str(primes[pos]) +'\n')








