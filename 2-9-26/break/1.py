#Find the first even digit from the left in 753914286.
n=753914286
while n>0:
    a=n%10
    if a%2==0:
        print(a)
        break
    n=n//10