#static methods
#without input and with out return
class StaticMethod:
    @staticmethod
    def method1():
        print("This is a static method.")
StaticMethod.method1()  
# Output: This is a static method.
#with input and with out return
class StaticMethod1:
    @staticmethod
    def method1(name):
        print(f"Hello, {name}!")
StaticMethod1.method1("Alice")
#without input and with  return
class StaticMethod2:
    @staticmethod
    def method1():
        return "This is a static method with return."
s=StaticMethod2.method1()
print(s)
##with input and with  return
class StaticMethod3:
    @staticmethod
    def method1(name):
        return f"Hello, {name}!"
t=StaticMethod3.method1("Bob")
print(t)
# combination of all methods in one class collage
class Collage:
    @staticmethod
    def student_details(name, course):
        return f"Student Name: {name}, Course: {course}"
    @staticmethod
    def grades(grade):
        return f"Grade: {grade}"
    #without input and with out return
    @staticmethod
    def collage_info():
        print("Welcome to ABC Collage!")
    #with input and with out return
    @staticmethod
    def event_details(event):
        print(f"Event: {event}")
    #without input and with return
    @staticmethod
    def location_info():
        return "Location: Main Street, City: New York"
a=Collage
a.collage_info()
print(a.student_details("John Doe", "Computer Science"))
print(a.grades("A"))
a.event_details("Science Fair")
print(a.location_info())