
#Sum of Prime Numbers Find the sum of all prime numbers between 20 and 150.
s=0
for j in range(20,151,1):
    n=j
    c=0
    for i in range(1,n+1,1):
        if n%i==0:
            c=c+1
    if c==2:
        s+=n
print("Sum of all prime numbers between 20 and 150 is:",s)
