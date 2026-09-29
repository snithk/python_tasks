#Find the first number whose digit sum is 10.
for i in range(10,41,1):
    n=i
 
    sum=0
    while n>0:
        a=n%10
        sum+=a
        n=n//10
    if sum==10:
        print(i)
        break

