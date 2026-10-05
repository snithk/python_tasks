#Find the first number with exactly 3 divisors between 1 and 100.

for j in range(1,101,1):
    n=j
    c=0
    for i in range(1,n+1,1):
    
        
        if n%i==0:
        
            c+=1
    if c==3:
        print(j)
        break
        
