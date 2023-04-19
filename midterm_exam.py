
N = int(input("Enter a positive integer: "))
pFactor = 2
while (N >= (pFactor * pFactor)):
   while (0 == (N % pFactor)): # check if pFactor is a factor
       N = N // pFactor # remove the factor
       print(pFactor)
   pFactor = pFactor + 1 # move to the next factor
   # 