# Shape → Circle, Rectangle
class shape:
    def area(self):
        print("area of the shape")
class triangle(shape):
    def area(self):
        print("area of the triangle")

class rectanle(shape):
    def area(self):
        print("area of the reactangle")
s=shape()
s.area()
t=triangle()
t.area()
r=rectanle()
r.area()

class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def start(self):
        print("Car starts")


class Bike(Vehicle):
    def start(self):
        print("Bike starts")


v = Vehicle()
v.start()

c = Car()
c.start()

b = Bike()
b.start()