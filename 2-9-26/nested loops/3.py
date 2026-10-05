#Leap Years in a Range(Not Nested Loop Logic) Print all leap years between 1900 and 2026.
for i in range(1900 , 2027,1):
    n=i
    if (n%4==0 and n%100!=0) or n%400==0:
        print(n,end=" ")
