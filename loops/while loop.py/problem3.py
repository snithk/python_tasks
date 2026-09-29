#2.Find the average of digits in a given number.Example: 624 → (6 + 2 + 4) / 3 = 4
n=int(input("enter the number"))
a=n
sum=0
i=0
while n>0:

    d=n%10
    sum+=d
    n=n//10
    i+=1
avg=sum//i
print(f'avg of {a} digits is {avg} ')