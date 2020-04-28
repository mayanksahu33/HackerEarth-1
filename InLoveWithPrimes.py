"""
Arjit challenges Deepa that if she can divide the weight of the cake as sum of two prime numbers between them, she can have the entire cake - and if she fails to do so, he'll get the cake.

The argument is getting more, and more heated now - please help them sort out their stupid arguments or an easier way would be to help them figure out who is going to have the cake.
"""


def SieveOfEratosthenes(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1):
        isPrime[i] = True
    p = 2
    while(p*p <= n):
        if (isPrime[p] == True):
            i = p*p
            while(i <= n):
                isPrime[i] = False
                i += p
        p += 1

def isSumOfPrimes(n):
    isPrime = [0] * (n+1)
    SieveOfEratosthenes(n, isPrime)
    for i in range(0, n):
        if (isPrime[i] and isPrime[n - i]):
            print("Deepa")
            return
    print("Arjit")
    return

T = int(input())
for _ in range(T):
    n = int(input())
    hahaah = isSumOfPrimes(n)
