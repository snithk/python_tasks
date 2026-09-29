#Extract 1432578, skipping odd digits.
n=1432578
sum=0
while n>0:
    a=n%10
    if a%2!=0:
        n=n//10
    else:
        sum=sum*10+a
        n=n//10
print(sum)