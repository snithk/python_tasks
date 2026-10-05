#Extract 5832461, printing only even digits.
n=5832461
sum=0
while n>0:
    a=n%10
    if a%2==0:
        sum=sum*10+a
        n=n//10
    else:
        n=n//10
print(sum)