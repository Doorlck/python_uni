# n=int(input())
# pi=3.1415926535
# e1=2.7182818284
# e2=2.71828182845904523536
# c1=((2*pi*n)**(1/2))*n**n*e1**(n*(-1))
# c2=((2*pi*n)**(1/2))*n**n*e2**(n*(-1))
# print(c1)
# print(c2)
# print(c1-c2)

e=2.7182818284
B=int(input())
r=int(input())
w=int(input())
T=int(input())
z1=float(input())
z2=float(input())
A1=B*e**((r-1/2*w**2)*T+w*T**(1/2)*z1)
A2=B*e**((r-1/2*w**2)*T+w*T**(1/2)*z2)
print(A1,A2)


