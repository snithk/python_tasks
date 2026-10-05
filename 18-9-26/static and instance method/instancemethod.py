#without input and with out return
class InstanceMethod:
    def method1(self):
        print("This is an instance method.")
InstanceMethod().method1() 
     # Output: This is an instance method.
##with input and with out return
class InstanceMethod1:
    def method1(self, name):
        print(f"Hello, {name}!")
a=InstanceMethod1()
a.method1("Alice")
##without input and with return
class InstanceMethod2:
    def method1(self):
        return "This is an instance method with return."
c=InstanceMethod2()
print(c.method1())
#with input and with return
class InstanceMethod3:
    def method1(self, name):
        return f"Hello, {name}!"
d=InstanceMethod3()
print(d.method1("Bob"))

# combination of all methods in one class bank
class Bank:
    def employee_details(self, name, position):
        return f"Employee Name: {name}, Position: {position}"
    def account_balance(self, balance):
        return f"Account Balance: ${balance}"
    #without input and with out return
    def bank_info(self):
        print("Welcome to XYZ Bank!")
    #with input and with out return
    def transaction_details(self, amount):
        print(f"Transaction Amount: ${amount}")
    #without input and with return
    def branch_info(self):
        return "Branch: Main Street, City: New York"
a=Bank()

a.account_balance(1000)
a.transaction_details(500)
a.employee_details("John Doe", "Manager")
a.bank_info()
print(a.bank_info()   )
print(a.branch_info())
print(a.employee_details("John Doe", "Manager"))
print(a.account_balance(1000))
