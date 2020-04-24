"""
Given an array of positive and negative integers, denoting different types of parentheses. The positive numbers  denotes opening parentheses of type  and negative number  denotes closing parentheses of type .

Open parentheses must be closed by the same type of parentheses. Open parentheses must be closed in the correct order, i.e., never close an open pair before its inner pair is closed (if it has an inner pair). Thus,  is balanced, while  is not balanced.

You have to find out the length of the longest subarray that is balanced.
"""




n = int(input())
a = list(map(int,input().split()))
s = []
ans = 0
 
for i in range(n):
    if a[i] > 0:
        s.append(i)
    elif a[i] < 0:
        if s and a[i] == -a[s[-1]]:
            s.pop()
            if not s:
                temp = -1
            else:
                temp = s[-1]
            ans = max(ans,i - temp)
        else:
            s.append(i)
print(ans) 

