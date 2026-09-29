#5.Find the difference between the largest digit and the smallest digit in a given number.
# Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7
n=int(input("enter the number"))
a=n
sum=0
l=0
s=9
while n>0:

    d=n%10
    if d>l:
        l=d
    if d<s:
        s=d
    n=n//10
diff=l-s
print(f'difference of {l} and {s} digits is {diff} ')