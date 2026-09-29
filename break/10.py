#Print the first 3 numbers divisible by 7.
c=0
for i in range(1,101,1):
    n=i
    s=n
    a=n%10
    a=a*2
    n=n//10
    sum=n-a

    if sum%7==0:
        print(i)
        c+=1
        if c==3:
            break
