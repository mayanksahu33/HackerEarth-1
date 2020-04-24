"""
Given a string, convert it into its number form .

A or a -> 1
B or b -> 2
C or c -> 3
. . .
Z or z -> 26
space -> $


"""




Q = int(input())

for i in range(Q):
    string = input()
    aux = []
    for c in string:
        if c == ' ':
            aux.append("$")
        else:
            if ord(c) in range(97,123): #an einai mikro
                dif = ord(c) - ord("a")
                # print(c,"a",dif)
                aux.append(dif+1)
            else: #an einai kefalaio
                dif = ord(c) - ord("A")
                # print(c,"A",dif)
                aux.append(dif+1)
    # print(aux)
    print(''.join(str(e) for e in aux))
  
