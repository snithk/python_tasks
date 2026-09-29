#Maximum Factors
#Find the number between 50 and 150 that has the maximum number of factors.
maxium=0
height_factor=0
for j in range(50,151,1):
    n=j
    c=0
    for i in range(1,n+1,1):
        if n%i==0:
            c+=1
   
    if c>maxium:
        maxium=c
        height_factor=j
print(f"{ height_factor} has {maxium}")

    
    