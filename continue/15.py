#Extract 502304, skipping digit 0.
n=502304
sum=0
while n>0:
    a=n%10
    if a==0:
        n=n//10
    else:
        sum=sum*10+a
        n=n//10
print(sum)
