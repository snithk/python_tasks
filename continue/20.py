#Print 1–500, skipping numbers containing digit 0.

for i in range(1,501,1):
    s=False
    n=i
    while n>0:
        a=n%10
        if a==0:
            s=True
            break
        n=n//10
    if s:
        continue
    print(i,end=" ")