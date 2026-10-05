'''4.Calculate the discount based on shopping amount.
    Below ₹1,000 → No discount, ₹1,000–₹4,999 → 10%, ₹5,000–₹9,999 → 20%, ₹10,000 and above → 30%.
'''
n=int(input("enter the amount: "))
if n<1000:
    print('No discount')
elif n>1000 and n<5000:
    print("10%' discount")
elif n>5000 and n<10000:
    print("20%' discount")
else:
     print("30%' discount")