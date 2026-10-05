class person:
    def name(self):
        print("name: ravi")
    def age(self):
        print("age is 34")
class employee(person):
    def id(self):
        print("employee id 21212")
    def salary(self):

        print("salary 200000")

class manger(employee):
    def deparment(self):
        print("deparment is marketing")
m=manger()
m.name()
m.age()
m.id()
m.salary()
m.deparment()


class Animal:
    def detalis(self):
        print(self.name)
        print(self.age)
class dog(Animal):
    def bread(self):
        print(self.bread)
class puppy(dog):
    def __init__(self,name,age,bread,training_level):
        self.name=name
        self.age=age
        self.bread=bread
        self.training_level=training_level
    def animaldetail(self):
        super().detalis()
        super().bread()
        print("trainginglevel is",self.training_level)
p=puppy("ravi",25,"puppy","l5")
p.animaldetail()
#
class Camera:
    def __init__(self, megapixel):
        self.megapixel = megapixel


class Phone:
    def __init__(self, brand):
        self.brand = brand


class Smartphone(Camera, Phone):
    def __init__(self, megapixel, brand):
        Camera.__init__(self, megapixel)
        Phone.__init__(self, brand)

    def display(self):
        print("Brand =", self.brand)
        print("Camera =", self.megapixel, "MP")


s = Smartphone(108, "Samsung")
s.display()

class Teacher:
    def __init__(self, subject):
        self.subject = subject


class Researcher:
    def __init__(self, research_area):
        self.research_area = research_area


class Professor(Teacher, Researcher):
    def __init__(self, subject, research_area):
        Teacher.__init__(self, subject)
        Researcher.__init__(self, research_area)

    def display(self):
        print("Subject =", self.subject)
        print("Research Area =", self.research_area)


p = Professor("Python", "Artificial Intelligence")
p.display()
        
