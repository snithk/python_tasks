'''
111111111
 2222222
  33333
   444
    5
'''
for i in range(1,6,1):
    for j in range(1,i,1):
         print(" ",end="")
    for j in range(5,i-1,-1):
         print(i,end="")
    for j in range(i,5,1):
         print(i,end='')
    
    print()