'''
    1
   222
  33333
 4444444
555555555
'''
for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1,1):
        print(i,end="")
    for j in range(i,1,-1):
        print(i,end="")
    print()