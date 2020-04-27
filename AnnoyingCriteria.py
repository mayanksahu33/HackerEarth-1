"""
A company follows a very annoying process of shortlisting applicants for a job. They calculate the value of the applicant's name by adding position of alphabet from 1-26 and then finding number of divisors for the name value. If the divisor number exceeds length or equal to length of name the person is IN, otherwise OUT.

"""



T = int(input())

def len_factors(x):
    res = []
    for i in range(1, x + 1):
        if x % i == 0:
            res.append(i)
    return len(res)


for _ in range(T):
    string = [str(a) for a in input()]
    aux = 0
    for c in string:
        if ord(c) in range(97,123): #an einai mikro
            dif = ord(c) - ord("a") + 1
        else: #an einai kefalaio
            dif = ord(c) - ord("A") + 1
        aux += dif

    if len_factors(aux) >= len(string):
        print("IN")
    else:
        print("OUT")



