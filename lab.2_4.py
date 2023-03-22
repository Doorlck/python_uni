a,b,c,d,e,f=1,2,3,4,5,6
res=0

#1
res = a+b **c*d//e-f
print(res,"=a+b**c*d//e-f",sep="")
#2
res = (a+b)**c*d//e-f
print(res,"=(a+b)**c*d//e-f",sep="")
#3
res=((a+b)**c)*d//e-f
print(res,"=((a+b)**c)*d//e-f",sep="")
#4
res=a+b**c*(d//(e-f))
print(res,"=a+b**c*(d//(e-f)",sep="")