#Check whether a given triangle is a valid triangle or not.
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
n3=int(input("enter the number:"))
sum=n1+n2
if sum>n3:
    print("it is a valid triangle")
else:
     print("it is not a valid triangle")