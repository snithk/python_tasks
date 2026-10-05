"""
.Display the age category.
    Below 13 → Child, 13–19 → Teenager, 20–59 → Adult, 60 and above → Senior Citizen.
"""
n=int(input("enter the age :"))
if n<13:
    print("child")
elif n>13 and n<19:
    print(' Teenager')
elif n>20 and n<59:
    print('Adult,')
else:
    print('Senior Citizen.')