#calculate the electric bills abased on the units
units=int(input("enter the electric bill units: "))
if units<=100:
    print("₹2/unit")
elif units>=101 and units<=200:
    print("₹4/unit")
elif units>=201 and units<=300:
    print("₹6/unit")
elif units>=301:
    print("₹8/unit")
#leaf year
a=int(input("enter the year"))
if a%400 == 0 or a%4==0 and a%100==0 :
    print("leaf Year")
else:
    print("not leaf year")
