#Extract 8325147, print digits until 5.
n=8325147
sum=0
while n>0:
    a=n%10
    if a==5:
        break
    sum=sum*10+a
    n=n//10
print(sum)
