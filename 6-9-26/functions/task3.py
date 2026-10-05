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
