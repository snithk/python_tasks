#3.Find the sum of the first digit and the last digit of a given number.Example: 936 → 9 + 6 = 15
n=int(input("enter the number"))
a=n
sum=0
i=0
while n>0:

    d=n%10
    if i==0:
        sum+=d
   
    n=n//10
    if n==0:
        sum+=d
    i+=1
print(f"sum of the first digit and last of the {a} is {sum}")