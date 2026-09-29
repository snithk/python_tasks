'''
3.Check whether a student is eligible for a scholarship.
    Age should be above 18. If eligible by age, score should be above 86.
'''
age=int(input("enter the age : "))
if age>18:
    score=int(input("enter the marks"))
    if score>66:
        print("your eligible for scholarship ")
    else:
        print("your score not eligible for scholarship ")
else:
    print("your not age  eligible for scholarship ")