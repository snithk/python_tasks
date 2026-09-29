#1.Check whether a given number is a 3-digit number or not.
"""n=int(input())

sum=1
for i in range(1,n+1,1):
    print(sum)
    sum*=3"""
'''
    1
   121
  12321
 1234321
123454321
'''
'''
for i in range(1,6,1):
    for j in range(5,i,-1):
         print(" ",end="")
    for j in range(1,i+1,1):
         print(j,end="")
    for j in range(i-1,0,-1):
         print(j,end='')
    
    print()
'''
'''
543212345
 5432345
  54345
   545
    5
'''
'''
for i in range(1,6,1):
    for j in range(1,i,1):
         print(" ",end="")
    for j in range(5,i-1,-1):
         print(j,end="")
    for j in range(i+1,6,1):
         print(j,end='')
    
    print()    
'''  
'''
123454321
 1234321
  12321
   121
    1
'''  
'''
for i in range(5,0,-1):
    for j in range(5,i,-1):
         print(" ",end="")
    for j in range(1,i+1,1):
         print(j,end="")
    for j in range(i-1,0,-1):
         print(j,end='')
    
    print() 
    '''
'''
* * * * * 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
'''
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1:
         print("*",end=" ") 
        else:
            print(j,end=" ")
    print()
'''
'''
* * * * * 
1 2 3 4 5 
* * * * * 
1 2 3 4 5 
* * * * * 
'''
'''
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i==3 or i==5:
         print("*",end=" ") 
        else:
            print(j,end=" ")
    print()
'''
'''
* 2 * 4 * 
* 2 * 4 * 
* 2 * 4 * 
* 2 * 4 * 
* 2 * 4 * 
'''
'''
for i in range(1,6,1):
    for j in range(1,6,1):
        if j==1 or j==3 or j==5:
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
'''
"""
1 2 * 4 5 
1 2 * 4 5 
* * * * * 
1 2 * 4 5 
1 2 * 4 5 
"""
"""
for i in range(1,6,1):
    for j in range(1,6,1):
        if i==3 or j==3 :
         print("*",end=" ") 
        else:
            print(j,end=" ")
    print()
"""
"""
* * * * * * * 
*           * 
*           * 
*           * 
*           * 
*           * 
* * * * * * * 
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if i==1 or i==7 or j==1 or j==7:
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
"""
"""
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if i==1 or i==4 or i==7 or j==1 or j==4 or j==7:
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
"""
"""
* * * *       
      *       
      *       
      *       
      *       
      *       
      *       
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if (i==1 and j<=4 )or j==4:
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
"""
"""
* * * *       
      *       
      *       
      *       
      *       
      *       
      * * * * 
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if (i==1 and j<=4 )or j==4 or(i==7 and j>=4):
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
"""
"""
* * * *     * 
      *     * 
      *     * 
* * * * * * * 
*     *       
*     *       
*     * * * * 
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if (i==1 and j<=4 )or j==4 or(i==7 and j>=4) or i==4 or (j==7 and i<=4) or (j==1 and i>=4):
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
"""
"""
            * 
          *   
        *     
      *       
    *         
  *           
*             
"""
"""
for i in range(7,0,-1):
    for j in range(1,8,1):
        if (i==j):
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
"""
"""
            * 
          *   
        *     
      *       
    *         
  *           
*             
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if i+j==7:
         print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
"""
"""
* * * * * * * 
* *   *   * * 
*   * * *   * 
* * * * * * * 
*   * * *   * 
* *   *   * * 
* * * * * * * 
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if i+j==8 or i==1 or i==4 or i==7 or j==1 or j==4 or j==7 or(i==j) :
         print("*",end=" ") 
        
        else:
            print(" ",end=" ")
    print()
"""
"""
*           * 
  *       *   
    *   *     
      *       
      *       
      *       
      * 
"""
"""
for i in range(1,8,1):
    for j in range(1,8,1):
        if (i==j and i<=4 and j<=4) or (j==4 and i>=4) or (i+j==8 and j>=4 and i<=4):
         print("*",end=" ") 
        
        else:
            print(" ",end=" ")
    print()
"""
"""
* * * * * * * * * * 
                  * 
                  * 
                  * 
* * * * * * * * * * 
*                   
*                   
*                   
* * * * * * * * * * 
"""
"""
for i in range(1,10,1):
    for j in range(1,11,1):
        if i==1 or (j==10 and i<=5) or i==5 or (j==1 and i>=5) or i==9:
        
            print("*",end=" ")
        else:
            print(" ",end=" ")
       
    print()
"""
'''
        *         
      *   *       
    *       *     
  * * * * * * *   
*               * 
'''
'''
for i in range(1,7,1):
    for j in range(1,10,1):
        if (i+j==6 ) or(i==2 and j==6)  or (i==3 and j==7) or (i==4 and j==8) or (i==5 and j==9) or(i==4 and j>=3 and j<=7):
        
            print("*",end=" ")
        else:
            print(" ",end=" ")
       
    print()
'''
'''
for i in range(1,10,1):
    for j in range(1,10,1):
        if (i==1) or (j==1  or (i==1)) or (i==9 and j<=5) or(j==5 and i>=5) or (i==5 ) or j==9 and i>=5:
        
            print("*",end=" ")
        else:
            print(" ",end=" ")
       
    print()
'''
n=101
b=n
sum=0
while n>0:
    a=n%10
    sum=sum*10+a
    n=n//10

if b==sum:
    print(b)