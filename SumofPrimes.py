"""
In Short, for each function  you need to find the summation of all primes between the integers l and r inclusive.
"""

T = int(input())
 

from bisect import bisect_left
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
 
 
def savePrimes(l,u): 
    lista = list(range(l,u+1))
    return sum(list(filter(isPrime,lista)))
 
 
 
 
for i in range(T):
    l , u = list(map(int,input().split()))
    print(savePrimes(l,u))
