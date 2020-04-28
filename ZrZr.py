"""
You are given a number N. How many zeroes does N! end on?

"""
T = int(input())
import math
for _ in range(T):
    n = int(input())
    # print(int(math.log(n,5)))
    cnt = 0
    while n > 0:
        cnt += n // 5
        n = n //5
        
    print(cnt)
