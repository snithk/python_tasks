#.Display the grade based on average only if the student has passed in all 4 subjects.
sub1=int(input("enter the marks: "))
sub2=int(input("enter the marks: "))
sub3=int(input("enter the marks: "))
sub4=int(input("enter the marks: "))

if sub1>=50 and  sub2>=50 and sub3>=50 and sub4>=50:
    sum=sub1+sub2+sub3+sub4
    avg=sum//4
    if avg>=50 and avg<=59:
        print("Grade D")
    elif avg>=60 and avg<=69:
            print("Grade C")
    elif avg>=70 and avg<=79:
            print("Grade B")
    else:
           print("Grade A")
else:
    print("fail")
