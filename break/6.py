#Find the first palindrome between 10 and 500.
for i in range(10,501,1):
    n=i
    sum=0
    while n>0:
        a=n%10
        sum=sum*10+a
        n=n//10
    if sum==i:
        print(i)
        break