'''
                  
        *         
      *   *       
* * * * * * * * * 
  *           *   
* * * * * * * * * 
      *   *       
        *         
               
'''
'''
for i in range(1,10,1):
    for j in range(1,10,1):
        if i==6 or (i+j==7 and i>=2) or(i==3 and j==6) or (i==4 and j==7)or (i==5 and j==8) or i==4 or (i==7 and j==4)or  (i==8 and j==5) or (i==7 and j==6):

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
'''
        *         
      *   *       
* * * * * * * * * 
  *           *   
* * * * * * * * * 
      *   *       
        *  

'''
for i in range(1,8,1):
    for j in range(1,10,1):
        if i==5 or (i+j==6 )  or(j-i==4) or i==3 or(i-j==2) or (i+j==12):

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
*               * 
*               * 
*               * 
*       *       * 
*     *   *     * 
*   *       *   * 
* *           * * 
"""
"""
for i in range(1,8,1):
    for j in range(1,10,1):
        if j==1 or j==9 or (i+j==9 and i>=4) or (j-i==1 and i>=4):

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
