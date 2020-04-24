






Q = int(input())
for i in range(Q):
    a, b, c = list(map(int,input().split()))
    s = set()
    s.add(a)
    l = [a]
    flag = True
    cnt = 0
    while(flag):
        l1 = list(map(lambda a : a * c,l))
        l2 = list(map(lambda a : a -1,l))
        l3 = list(map(lambda a : a -2,l))
        l = list( set(l1).union(set(l2).union(set(l3))))
        cnt += 1
        s = set(l).union(s)
        if b in s:
            flag = False
    print(cnt)
        # print(s)
