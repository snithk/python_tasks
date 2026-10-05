class Employee:
    def work(self):
        print("does general work")
class Developer(Employee):
    def work(self):
        print("develop the application")
class SeniorDeveloper:
    def work(self):
        print("check the code")

e=Employee()
e.work()
d=Developer()
d.work()
s=SeniorDeveloper()
s.work()

class Vehicle:
    def speed(self):
        print("Vehicle has speed")


class Car(Vehicle):
    def speed(self):
        print("Car has normal speed")


class SportsCar(Car):
    def speed(self):
        print("Sports car has high speed")


v = Vehicle()
v.speed()

c = Car()
c.speed()

s = SportsCar()
s.speed()