#1.Check whether a given number is a 3-digit number or not.
n=int(input("enter the number:"))
if len(str(n))==3:
    print(f"{n} is a three digit number")
else:
    print(f"{n} is not a three digit number")