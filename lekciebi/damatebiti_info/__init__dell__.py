# __init__ მაგიკური მეთოდი ინით - შექმნა
#__dell__ მაგიკური მეთოდი დელ - წაშლა - დესტრუქტორი



class Lekciebi:
    def __init__(self, name, teacher, duration):
        self.name = name
        self.teacher = teacher
        self.duration = duration

    def __del__(self):
        print(f"Lesson '{self.name}' has been deleted.")


name = input("Введите название урока: ")
teacher = input("Введите имя преподавателя: ")
duration = int(input("Введите продолжительность урока в минутах: "))

lesson1 = Lekciebi(name, teacher, duration)

print("Название урока:", lesson1.name)
print("Преподаватель:", lesson1.teacher)
print("Продолжительность:", lesson1.duration, "минут")