'''
*       * * * * * 
*       *         
*       *         
*       *         
* * * * * * * * * 
        *       * 
        *       * 
        *       * 
* * * * *       * 
'''
''''''
for i in range(1,10,1):
    for j in range(1,10,1):
        if (j==1 and i<=5) or i==5 or (j==9 and i>=5) or (i==1 and j>=5) or j==5 or (i==9 and j<=5):
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
        
