"""
Given a 10^6 * 10^6 matrix with each cell initially consisting of zero values. The input given consists of 
co-ordinates of cells which have to be marked as 1. Let’s call them true cells. We have to find the number of 
pairs of such true cells which are in the same diagonal.

Can you help him out?

"""

from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    ans=0
    d1=defaultdict(int)
    d2=defaultdict(int)
    for i in range(n):
        x ,y = map(int,input().split())
        ans+=d1[a+b]
        ans+=d2[a-b]
        d1[a+b]+=1
        d2[a-b]+=1
    print(ans)


