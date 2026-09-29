
#Digit Sum = 10
#Print all numbers between 120 and 850 whose digit sum is exactly 10.
for i in range(120,850):
    a=i
    sum=0
    while a>0:
        b=a%10
        sum+=b
        a=a//10
    if sum==10:
        print(i,end=" ")
