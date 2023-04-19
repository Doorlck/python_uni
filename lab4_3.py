#n-way if statement
n=int(input('후후'))
if n<1 :
    print('tiny')
elif n<5 :
    print('small')
elif n<15 :
    print('medium')
elif n<50 :
    print('large')
elif n<150 :
    print('huge')
else :
    print('gigantic')
