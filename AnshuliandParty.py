"""
Vishi's birthday is on the door.
Anshuli and his friends are planning to give him a birthday party. For that Anshuli's friends want him to buy the cake. He needs to pay 'x' amount of money to buy the cake on the first day. After each day has passed, the cake becomes 'x' times the price that it was on the previous day. For buying the cake Anshuli has to collect money from all the friends and for that, he will need 'y' days and after 'y' days he will go and buy the cake.
Anshuli seeks your help in calculating the price of cake on the yth day.
Take the price as modulo 10^9 + 7 as the price can be very large.
"""


N = int(input())
const = pow(10,9) + 7

for i in range(N):
    x , y = list(map(int,input().split()))
    print(pow(x % const,y,const) % const)






