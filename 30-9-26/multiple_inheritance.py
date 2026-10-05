class Teacher:
    def work(self):
        print("Teacher teaches students")

class Researcher:
    def work(self):
        print("Researcher conducts research")

class Professor(Teacher, Researcher):
    def work(self):
        print("Professor teaches and conducts research")

t = Teacher()
t.work()

r = Researcher()
r.work()

p = Professor()
p.work()

class Engine:
    def start(self):
        print("Engine starts")

class MusicSystem:
    def start(self):
        print("Music system starts")

class Car(Engine, MusicSystem):
    def start(self):
        print("Car starts with engine and music system")

e = Engine()
e.start()

m = MusicSystem()
m.start()

c = Car()
c.start()