"""
You are a bank account hacker.Initially you have 1 rupee in your account, and you want exactly N rupees in your 
account.You wrote two hacks, First hack can multiply the amount of money you own by 10, while the second can 
multiply it by 20. These hacks can be used any number of time . Can you achieve the desired amount N using these 
hacks.

"""
Q = int(input())
s = set()
s.add(1)
l = [ 1 ]
for i in range(12):
    l1 = list(map(lambda a : a*10,l))
    l2 = list(map(lambda b : b*20,l))
    l = list( set(l1).union(set(l2)) )
    for i in l:
        s.add(i)
for i in range(Q):
    n = int(input())
    if n in s:
        print ("Yes")
    else:
        print ("No")
