#Extract 5830421, skip odd digits, stop at 0.
n=5830421
sum=0
while n>0:
    a=n%10

    if a%2!=0:
        n=n//10
        continue
    if a==0:
        break
    sum=sum*10+a
    n=n//10
print(sum)
