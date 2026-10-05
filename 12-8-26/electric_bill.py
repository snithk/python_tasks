#calculate the electric bills abased on the units
units=int(input("enter the electric bill units: "))
billaount=0
if units<=100:
    print("₹2/unit")
    billaount+=(units*2)
elif units>=101 and units<=200:
    billaount+=(100*2)+(units-100)*4
    print("₹4/unit")
elif units>=201 and units<=300:
    billaount+=(100*2)+(200*4)+(units-200)*6
    print("₹6/unit")
else :
    billaount+=(100*2)+(200*4)+(300*6)+(units-300)*8
    print("₹8/unit")
print("total amount: ",billaount)
#leaf year
a=int(input("enter the year"))
if a%400 == 0 or a%4==0 and a%100==0 :
    print("leaf Year")
else:
    print("not leaf year")
