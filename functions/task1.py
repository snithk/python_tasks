#with out input and with out return

#Sum of Prime Numbers Find the sum of all prime numbers between 20 and 150.

def Sum_of_Prime():
    s=0
    for j in range(20,151,1):
        n=j
        c=0
        for i in range(1,n+1,1):
            if n%i==0:
                c=c+1
        if c==2:
            s+=n
    print("Sum of all prime numbers between 20 and 150 is:",s)

#Print 1–50, skip multiples of 3.
def skip_multiples_of_3():
    for i in range(1,51,1):
        if i%3==0:
            continue
        
        print(i,end=" ")
#Print 1–200, skipping multiples of 3 or 5.
def skip_multiples_of_3_and_5():
    for i in range(1,201,1):
        if i%3==0 or i%5==0:
            continue
        print(i,end=" ")
#factorical of the number
def factorical():
    n=4
    mul=1
    for i in range(n,0,-1):
        mul=mul*i
    print(f"factorical of {n}! = {mul}")
# given number is odd or not
def odd():
    n=5
    for i in range(0,n-1,-1):
        if i%2 !=0:
            print(i)
#count the number the digits
def count_digits():
    n=345
    i=0
    while n>0:
        i+=1
        n=n//10
    print(i)
##with out input and with out return

#Sum of Prime Numbers Find the sum of all prime numbers between 20 and 150.

def Sum_of_Prime():
    s=0
    for j in range(20,151,1):
        n=j
        c=0
        for i in range(1,n+1,1):
            if n%i==0:
                c=c+1
        if c==2:
            s+=n
    print("Sum of all prime numbers between 20 and 150 is:",s)

#Print 1–50, skip multiples of 3.
def skip_multiples_of_3():
    for i in range(1,51,1):
        if i%3==0:
            continue
        
        print(i,end=" ")
#Print 1–200, skipping multiples of 3 or 5.
def skip_multiples_of_3_and_5():
    for i in range(1,201,1):
        if i%3==0 or i%5==0:
            continue
        print(i,end=" ")
#factorical of the number
def factorical():
    n=4
    mul=1
    for i in range(n,0,-1):
        mul=mul*i
    print(f"factorical of {n}! = {mul}")
# given number is odd or not
def odd():
    n=5
    for i in range(0,n-1,-1):
        if i%2 !=0:
            print(i)
#count the number the digits
def count_digits():
    n=345
    i=0
    while n>0:
        i+=1
        n=n//10
    print(i)
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


#with out input and with return

#Find the sum even digit from the left in 753914286.
def sum_of_digits():
    n=753914286
    sum=0
    while n>0:
        a=n%10
        if a%2==0:
            sum+=a
    
        n=n//10
    return sum
a=sum_of_digits()
print(a)

# check guven number is perfect or not
def perfect():
    a=6
    sum=0
    for i in range(1,a,1):
        if a%i==0:
            sum+=i
    if sum==a:
        return  a ,"given number is perfect"
    else:
        return "given number is not perfect"
b=perfect()
print(b)
#Write a function to return the square of a number.
def square(n):
    return n*n
s=square(5)
print(s)
#Write a function to return the sum of all odd numbers from 1 to 50.
def sum_of_odd():
    sum=0
    for i in range(1,51,1):
        if i%2!=0:
            sum+=i
    return sum
a=sum_of_odd()
print(a)
#write a function to return the postive or negative 
def pos_neg(n):
    if n>0:
        return "given number is positive"
    else:
        return "given number is negative"
e=pos_neg(-5)
print(e)

#with input  and with return
# sum of the two numbers
def sum_of_two_numbers(a, b):   
    return a + b
#Print even numbers in the given number
def print_even_numbers(n):
    sum = 0
    while n > 0:
        a=n%10
        if a%2 == 0:
            sum = sum * 10 + a
        n =n//10
    return sum
print(print_even_numbers(1234567890))
#Find the triangle is equivalent or not
def is_equivalent_triangle(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False
#display age categories
def age_category(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"
#Simple interest based on principle,rate and time
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100  
#find the if the nuber is divisible by three and five
def is_divisible_by_three_and_five(n):
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False
#find the sum of digits of a number
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
#call all function above
print(sum_of_two_numbers(5, 10))
print(print_even_numbers(1234567890))
print(is_equivalent_triangle(5, 5, 5))
print(age_category(25))
print(simple_interest(1000, 5, 2))
print(is_divisible_by_three_and_five(15))
print(sum_of_digits(12345))

skip_multiples_of_3()
skip_multiples_of_3_and_5()
factorical()
sum_of_digits()
Sum_of_Prime()

