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