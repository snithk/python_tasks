#with input and with out return

# skip the odd numbers in the digit and stop at 0 digit in the given value
def skip_and_break(n):

    sum=0
    while n>0:
        a=n%10

        if a%2!=0:
            n=n//10
            continue
        if a==0:
            break
        sum=sum*10+a
        n=n//10
    print(sum)
n=5830421

#Extract 8325147, print digits until 5.
def print_digit(n):

    sum=0
    while n>0:
        a=n%10
        if a==5:
            break
        sum=sum*10+a
        n=n//10
    print(sum)
a=8325147

#Print 1–40, skipping multiples of 4.
def skip_mul_of_(n):
    for i in range(1,n+1,1):
        if i%4==0:
            continue
        print(i,end=" ")
e=40


#print given number is even or not
def even(a):
    if a%2==0:
        print("given number is even")
    else:
        print("given number is odd")
q=12

##wirte the code prin the sequence of 5,10,15,20
def print_seuence(a):
    i=0
    while(i<=a):
        if (i%5==0):
            print(i,end=" ")
        i=i+1
w=21


#find the sum of digits in given number

def sum_difits(a):
    sum=0
    while a>0:
        d=a%10
        sum+=d
        a=a//10
    print(sum)
sum_difits(23234)


