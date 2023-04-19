#exception handler
try :
    my_x=input("Enter x:")
    x= int(my_x)
    
except :
    x=1

y=10
z= x**y
print(x,'^',y,'=',z,sep='')
