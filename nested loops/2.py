# Average of Perfect Numbers Find the average of all perfect numbers between 1 and 1000.
s=0
c=0
for j in range(1,1001,1):
    n=j
    sum=0

    for i in range(1,n,1):
        if n%i==0:
            sum+=i
    if sum==n:
        s+=n
        c+=1
print(f"Average of all perfect numbers between 1 and 1000 is: {s//c}")

    
    
