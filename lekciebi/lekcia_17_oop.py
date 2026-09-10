# object oriented programming -> OOP
# class, object, attribute, method 

# 4 principi 

# კლასი - blueprint - > object
# method -> function 
# attribute -> saxeli, gvari, asaki....



class Dog:
    # konstruqtori
    def __init__(self, name, feature):  
        self.name = name
        self.feature = feature

    def show_info(self): # method
        print(f"{self.name} and {self.feature}")


dog_object = Dog("J", 'bark')   # object 
print(dog_object) 
dog_object.show_info()

dog_object_2 = Dog("JA", 'barks')
print(dog_object.name)
print(dog_object.feature)



# ----------------------------------------------------------------------------


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # def __str__(self): # Human-readable
    #     return f"{self.brand} and {self.color}"

    # def __repr__(self):
    #     return f"Car (brand, color)"


car_1 = Car("Wrangler", 'Blue')
print(car_1)

    