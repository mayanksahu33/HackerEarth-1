"""
You are given length of n sides, you need to answer whether it is possible to make n sided convex polygon with 
it.

"""



Q = int(input())
for i in range(Q):
    N = int(input())
    arr = list(map(int,input().split()))
    m = max(arr)
    s = sum(arr)
    if s - m > m :
        print("Yes") 
    else: 
        print("No")
        
