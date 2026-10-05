#Armstrong Numbers
#Print all Armstrong numbers between 100 and 999.
for i in range(100,1000,1):
    n=i
    e=n

    sum=0
    while n>0:
        a=n%10
    
        c=e
        d=0
        while c>0:
            d+=1
            c=c//10
        a=a**d

        sum=sum+a
        n=n//10
    if sum==i:
        print(i,end=" ")

    
    
        
