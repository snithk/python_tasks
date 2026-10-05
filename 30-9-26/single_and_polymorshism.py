#
class shape:
    def area(self):
        print("area of the shape")
class circle(shape):
    def area(self):

        print("pi r square")
s=shape()
s.area()
c=circle()
c.area()

class employee:
    def work(self):
        print("work accordingly")
class manager(employee):
    def work(self):
        print("manager work")
e=employee()
e.work()
m=manager()
m.work()





