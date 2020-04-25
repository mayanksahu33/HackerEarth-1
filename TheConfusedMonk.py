"""

The Monk wants to teach all its disciples a lesson about patience, since they are always in a hurry to do something crazy. To teach them this, he gives them a list of N numbers, which may or may not be distinct. The students are supposed to solve a simple Mathematical equation based on the array of these N numbers.

g(x) - GCD (a[ 0 ], a[ 1 ], a[ 2 ]... a[n-1] )
f(x) - (a[ 0 ] * a[ 1 ] * a[ 2 ]... * a[n-1] )
The value of the MonkQuotient is: 109 + 7.

The equation to be solved is: ( f(x)g(x) ) % MonkQuotient

"""





from fractions import gcd
from functools import reduce
def fog(power,arr,const):
    res = 1
    for i in arr:
        res = res * (pow(i,power) % const)
    return res % const

def find_gcd(list):
    x = reduce(gcd, list)
    return x

const = pow(10,9) + 7
N = int(input())
arr = list(map(int,input().split()))
print( fog(find_gcd(arr),arr,const) )

