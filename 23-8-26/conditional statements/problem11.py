'''
1.Check whether a person is eligible to donate blood.
    Age should be between 18 and 60. If eligible by age, weight should be above 50 kg.

'''
age=int(input("enter the age: "))

if age>=18 and age<=60:
    weight=int(input("enter the weight: "))
    if weight>=50:
        print("your eligible to donate blood")
    else:
        print("your not eligible to donate blood")
else:
    print("your not eligible to donate blood")