'''
55555
 4444
  333
   22
    1
    '''
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(i,end="")
    print()