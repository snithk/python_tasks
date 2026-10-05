'''
.Check whether a given year is a Leap Year or not.
    Condition 1: year % 400 == 0
    Condition 2: year % 4 == 0 and year % 100 != 0
'''
n=int(input("enter the year:  "))
if  (n%100!=0 and n%4==0) or n%400==0 :
    print(f"{n} is a leaf year")
else:
    print(f"{n} is not a leaf year")