
# დავალება  - შექმენით ლისტი, სადაც მომხმარებელს შეეკითხებით 5 სასურველ რიცხვს და ჩაამატეთ ეს რიცხვები ლისტში. თუ შემოყვანილი რიცხვია არის 100-ზე მეტი, დაამატეთ ვალიდაცია რომ ლისტში არ ემატებოდეს, დანარჩენი რიცხვებისთვის წაშალეთ ტიდან ყველა განმეორებადი ელემენტი: მაგალითად თუ 6 არის 2-ჯერ მხოლოდ ერთხელ დატოვეთ და ა.შ. საბოლოოდ გამოიტანეთ ამ ლისტში არსებული ელემენტების ჯამი

numbers = []

while len(numbers) < 5:

    try:
        number = int(input("შეიყვანეთ რიცხვი: "))

        if number > 100:
            raise ValueError("რიცხვი 100-ს აღემატება")

        numbers.append(number)

    except ValueError as error:
        print("შეცდომა:", error)
        print("გთხოვთ, შეიყვანოთ მხოლოდ ერთი მთელი რიცხვი 100-მდე.")
        continue


print("საწყისი რიცხვები:", numbers)


new_list = []

for number in numbers:
    if number not in new_list:
        new_list.append(number)

print("რიცხვები გამეორების გარეშე:", new_list)


total = 0

for number in new_list:
    total = total + number

print("რიცხვების ჯამი:", total)
