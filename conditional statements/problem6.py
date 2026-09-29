"""Calculate the electricity bill based on units consumed.
    0–100: ₹2/unit, 101–200: ₹3/unit, 201–300: ₹5/unit, above 300: ₹7/unit.
"""
n=int(input("enter the electricity units"))
if n>=300:
    print("₹7")
elif n<=200 and n>100:
    print("₹3")
elif n<=300 and n>200:
    print("₹5")
else:
    print("₹2")