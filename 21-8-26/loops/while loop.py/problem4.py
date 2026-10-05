#4.Find the average of digits that are divisible by 5 in a given number.
# Example: 12575 → Divisible by 5 digits: 5, 5, 5 → Average = (5 + 5 + 5) / 3 = 5
n=int(input("enter the number"))
a=n
sum=0
i=0
while n>0:

    d=n%10
    if d%5==0:
        sum+=d
        i+=1
    n=n//10
    
avg=sum//i
print(f'avg of {a} digits is {avg} ')