Q = int(input())
for i in range(Q):
    n = int(input())
    A =  list(map(int, input().split(' ') )) 
    m = -1
    for i in range(n):
        for j in range(n):
            tmp = abs(A[i] - A[j]) + abs(i-j)
            if ( m > tmp ):
                m = tmp

    print(m)
