# __init__ მაგიკური მეთოდი ინით - შექმნა
#__dell__ მაგიკური მეთოდი დელ - წაშლა - დესტრუქტორი



class Lekciebi:
    def __init__(self, name, teacher, duration):
        self.name = name
        self.teacher = teacher
        self.duration = duration

    def __del__(self):
        print(f"Lesson '{self.name}' has been deleted.")


name = input("გთხოვთ შეიყვანოთ გაკვეთილის სახელი: ")
teacher = input("გთხოვთ შეიყვანოთ პრეპოდავტელის სახელი: ")
duration = int(input("გთხოვთ შეიყვანოთ გაკვეთილის ხანგრძლივობა წუთებში: "))

lesson1 = Lekciebi(name, teacher, duration)

print("გაკვეთილის სახელი:", lesson1.name)
print("პრეპოდავტელი:", lesson1.teacher)
print("ხანგრძლივობა:", lesson1.duration, "წუთი")