"""
ou need to help Monk find the total number of distinct candidate Strings for it Modulo .
"""


import math
const = pow(10,9) + 7
T = int(input())
for i in range(T):
    N , K = list(map(int,input().split()))

    print( math.factorial(max(N,K)) // math.factorial(abs(N-K)) % const)
 


