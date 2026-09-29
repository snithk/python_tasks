#Print 1–500, skipping numbers with odd digit sum.
for i in range(1,501,1):
    n=i

    sum=0
    n
    while n>0:
        a=n%10
        sum+=a
        n=n//10
    print(sum)
    if sum%2==0:
        print(i,end=" ")