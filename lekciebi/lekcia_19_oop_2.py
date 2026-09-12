# polymorphism  - იგივე მეთოდის სახელები მაგრამ განსახვავებული ქცევა 

# class Cat:
#     def act(self):
#         print("CAT")

# class Dog:
#     def act(self):
#         print("DOG")

# # c = Cat()
# # c.act()

# def animal_feature(animal):   # animal classebi rac aris imis object
#     animal.act()

# c = Cat()
# d = Dog()

# animal_feature(c)
# animal_feature(d)


# ----------------------------------------------------------------------------------------

# abstraction - 

# აბსტრაქტული კლასი -> განსაზღვრავს რომ რაღაც იარსებებს 

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def move(self):
#         pass


# class Car(Vehicle):
#     def move(self):
#         print("es aris move-is carshii implementacia")

# class Nebismieri(Vehicle):
#     def move(self):
#         print("es aris nebismieris implementacia ")

# c = Car()
# c.move()

# n = Nebismieri()
# n.move()


# ----------------------------------------------------------------------------------------------------


# class Student:
#     klasis_cvladi = "Python School"

#     def __init__(self, name):
#         self.name = name

#     def show_data(self):
#         return f"Student name is {self.name}"

#     @classmethod
#     def show_school(cls):
#         return f"School is {cls.klasis_cvladi}"


# s1 = Student("Student 11")
# print(s1.show_data())
# print(Student.show_school())


# --------------------------------------------------------------------------------------------
# multiple inheritance + MRO (method Resolution Ordering )

# class Mother:
#     def skill(self):
#         print("Mother")

# class Father:
#     def skill(self):
#         print("Father")

# class Child(Mother, Father):
#     pass

# c = Child()
# c.skill()

# print(Child.mro())


# ----------------------------------------------------------------------------


class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

print(D.mro())

# ----------------------------------------------------------------------------------------------------------

# magic - __str__, __len__, __getitem__ .... 
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    

b = Book("Pride and prejudice", 300)
print(len(b))



