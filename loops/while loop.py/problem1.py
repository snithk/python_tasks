#1.Find the sum of digits in a given number.Example: 738 → 7 + 3 + 8 = 18
n=int(input("enter the number"))
sum=0
while n>0:

    d=n%10
    sum+=d
    n=n//10
print(sum)
