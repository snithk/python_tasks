#Check the type of triangle based on its sides.
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
n3=int(input("enter the number:"))
if n1==n2==n3:
    print("triangel is Equilateral")
elif n1 ==n2 and n2!=n3 or n2==n3 and n1!=n3:
    print("triangel is Isosceles")
else:
    print("triangel is Scalene")
