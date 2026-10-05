class phone:
    company="vivo"
    country = "China"
    def __init__(self,name,model,ram,storage,camers):
        self.name=name
        self.model=model
        self.ram=ram
        self.storage=storage
        self.camers=camers
    def displayDetails(self):
        print("phonecompany name:",phone.company)
        print("company country: ",phone.country)
        print("phone name: ",self.name)
        print("phone model: ", self.model)
        print("phone ram: ",self.ram)
        print("phone storage",self.storage)
        print("phone camers",self.camers)
p1 = phone("Vivo V40", "V40", "8GB", "128GB", "50MP")
p2 = phone("Vivo X100", "X100", "12GB", "256GB", "64MP")


class location:
    country = "India"
    state = "Telangana"

    def __init__(self, city, areaname, streetname, pincode):
        self.city = city
        self.areaname = areaname
        self.streetname = streetname
        self.pincode = pincode

    def display(self):
        print("Country:", location.country)
        print("State:", location.state)
        print("City:", self.city)
        print("Area:", self.areaname)
        print("Street:", self.streetname)
        print("Pincode:", self.pincode)


l1 = location("Hyderabad", "Kukatpally", "Main Road", 500072)




class student:
    college = "Malla Reddy University"
    location = "Maisammaguda, Hyderabad"

    def __init__(self, name, course, rollno, section):
        self.name = name
        self.course = course
        self.rollno = rollno
        self.section = section

    def displaystudentdetails(self):
        print("College:", student.college)
        print("Location:", student.location)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Roll No:", self.rollno)
        print("Section:", self.section)

class Bank:


    bank_name = "State Bank"
    country = "India"
 

    def __init__(self, name, account_no, account_type, balance):
       
        self.name = name
        self.account_no = account_no
        self.account_type = account_type
        self.balance = balance

    def displayDetails(self):
      
        print("Bank Name:", Bank.bank_name)
        print("Country:", Bank.country)
        print("Customer Name:", self.name)
        print("Account Number:", self.account_no)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)


b1 = Bank("Rahul", 12345, "Savings", 50000)
b2 = Bank("Sneha", 67890, "Current", 100000)

s1 = student("Rahul", "CSE", 101, "A")
print("--------phone details---------")
p1.displayDetails()

p2.displayDetails()
print("-------------------location details---------------")
l1.display()
print("-------------------------student details----------------------------")
s1.displaystudentdetails()
print("------------------- bank details ---------------------")

b1.displayDetails()
b2.displayDetails()




        


    
        