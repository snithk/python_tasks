#Find the first perfect number between 1 and 1000.
for j in range(1,1000,1):
    n=j
    sum=0
    for i in range(1,n,1):
        if n%i==0:
            sum+=i
    if sum==n:
        print(n)
        break

