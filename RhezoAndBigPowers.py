"""
Rhezo likes numbers of the form . But computing , for any 2 numbers A and B is ahard task for him. He would like you to help him out in this.

"""

const = pow(10,9) + 7
x , y = int(input()) ,int(input())
print(pow(x % const,y,const) % const)




