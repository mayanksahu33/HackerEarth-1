'''
Joy is a hacker at hackerclub and he got a new problem on prime numbers.The problem states that given an integer N find the nearest prime number to N.If multiple answer is possible then output the smallest one of them.There are T number of test cases.
'''

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


def savePrimes(n): 
    lista = list(range(2,n))
    return list(filter(isPrime,lista))



primes = savePrimes(pow(10,6))

for i in range(T):
    n = int(input())
    if n in primes:
        print(n)
    else:
        pos = bisect_left(primes,n)
        r1 = primes[pos]
        r2 = primes[pos-1]
        if abs(r1 - n) >= abs(r2 -n):
            print(r2)
        else:
            print(r1) 
        










