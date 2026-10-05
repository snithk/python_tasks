class emplyee:
    def salary(self):
        print("salary 10000")
class teachers(emplyee):
    def pf(self):
        print("pdf amount is 2000")
e=teachers()
e.salary()
e.pf()

class bankaccount:
    def __init__(self,name,bankname):
        self.name=name
        self.bankname=bankname
    def display(self):
        print("name: ",self.name)
        print("bankname: ",self.bankname)

class savingaccount(bankaccount):
    def __init__(self,name, bankname, accountnumber,balance):
        super().__init__(name, bankname)
        self.account_no=accountnumber
        self.balance=balance
    def details(self):
        super().display()
        print("account_no number:",self.account_no)
        print("balance: ", self.balance)
s=savingaccount("ravi","union bank",120039390029,1000)
s.details()

class Electronic_Device:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
class tv(Electronic_Device):
    def display(self):
        print("tv company",self.brand)
        print("tv price",self.price)
t=tv("sony",20000)
t.display()

class collage:
    def __init__(self,name,location):
        self.name=name
        self.location=location
class student(collage):
    def __init__(self, name, location,rollno):
        super().__init__(name, location)
        self.rollno=rollno
    def studentdetails(self):
        print("collage name",self.name)
        print("collage location",self.location)
        print("student rollno",self.rollno)
stu=student("mru","masiamagudha","2211cs040082")
stu.studentdetails()


