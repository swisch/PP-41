

# ---------------------------------------------------------------------------------------------------

# OOP პრინციპები - 
# ენკაფსულაცია, პოლიმორფიზმი, მემკვიდრეობა, აბსტრაქცია


# encapsulation - პირდაპირი წვდომის შეზღუდვა
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough amount")

    def get_balance(self):
        return self.__balance


owner_1 = BankAccount("owner 1", 100)
owner_1.deposit(45)
# print(owner_1.balance) -> pirdapiri wvdomis shezghudva
print(owner_1.get_balance())

owner_1.withdraw(87)
print(owner_1.get_balance())


# ----------------------------------------------------------------------------------------------------------

# inheritance - 

class Animal:    # mshobeli
    def act(self):
        print("Animal class")

class Dog(Animal):
    def acts(self):
        super().act()
        print("es aris shvilobilshi damatebuli")

    def new(self):
        print("es marto shvilobilshia")


# class F(Dog):  


d = Dog()
# a = Animal()
# a.act()
d.acts()







