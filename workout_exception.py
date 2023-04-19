#try-except

#enter working hours
try :
    hours=float(input('working hours:'))
except :
    hours=40
#enter min wage
try :
    minwage=int(input('minwage:'))
except :
    minwage=9600

# complete the salary
overtime=0
if hours > 40 :
    overtime = hours-40
salary=minwage*hours+minwage*overtime*0.5