#Exactly 3 Factors
#Print all numbers between 10 and 300 that have exactly 3 factors.
for j in range(10,300,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count+=1
    if count==3:
        print(n)