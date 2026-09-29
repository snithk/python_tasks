#Prime Factors
#Print the prime factors of every number between 20 and 50.
for k in range(20,51,1):
    n=k
    print(f"prime factor of th {k} is",end=" ")
    for i in range(1,n+1,1):
        
        if n%i==0:
            count=0
            for j in range(1,i+1,1):
                if i%j==0:
                    count+=1
            if count==2:
                print( i,end=" ")
    print()




