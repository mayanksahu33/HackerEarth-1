"""
In Short, for each function  you need to find the summation of all primes between the integers l and r inclusive.
"""




def SieveOfEratosthenes(l,n): 
    aux = []  
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 

            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(l,n + 1): 
        if prime[p]: 
            aux.append(p)
    return aux 

T = int(input()) 
for i in range(T):
    l , u = list(map(int,input().split()))
    print(sum(SieveOfEratosthenes(l,u)))