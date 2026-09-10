import time


# ============================================================
# შეკვეთების შემოწმების დეკორატორი
# ============================================================

def validate_orders(func):

    def wrapper(orders):

        # სწორი სტატუსების სია
        valid_statuses = ["completed", "pending", "cancelled"]

        # გადავუყვებით ყველა შეკვეთას
        for order in orders:

            try:

                # ვამოწმებთ საჭირო გასაღებებს
                if "customer" not in order:
                    raise ValueError("აკლია customer გასაღები")

                if "product" not in order:
                    raise ValueError("აკლია product გასაღები")

                if "price" not in order:
                    raise ValueError("აკლია price გასაღები")

                if "quantity" not in order:
                    raise ValueError("აკლია quantity გასაღები")

                if "status" not in order:
                    raise ValueError("აკლია status გასაღები")


                # ფასი უნდა იყოს 0-ზე მეტი
                if order["price"] <= 0:
                    raise ValueError("ფასი უნდა იყოს 0-ზე მეტი")


                # რაოდენობა უნდა იყოს 0-ზე მეტი
                if order["quantity"] <= 0:
                    raise ValueError("რაოდენობა უნდა იყოს 0-ზე მეტი")


                # სტატუსი უნდა იყოს სწორი
                if order["status"] not in valid_statuses:
                    raise ValueError("შეკვეთის სტატუსი არასწორია")


            except ValueError as error:

                print()
                print("ნაპოვნია არასწორი შეკვეთა!")
                print("შეცდომა:", error)
                print("შეკვეთა:", order)

                return


        # თუ ყველა შეკვეთა სწორია,
        # ვიძახებთ შემდეგ ფუნქციას
        return func(orders)


    return wrapper


# ============================================================
# ფუნქციის შესრულების დროის გაზომვის დეკორატორი
# ============================================================

def execution_time(func):

    def wrapper(orders):

        # ვინახავთ ფუნქციის დაწყების დროს
        start_time = time.time()

        # ვიძახებთ ფუნქციას
        result = func(orders)

        # ვინახავთ ფუნქციის დასრულების დროს
        end_time = time.time()

        # ვითვლით შესრულების დროს
        total_time = end_time - start_time

        print()
        print("პროგრამის შესრულების დრო:", total_time)

        return result


    return wrapper


# ============================================================
# შეკვეთების ანალიზის დეკორატორი
# ============================================================

def analyze_orders(func):

    def wrapper(orders):

        print()
        print("======================================")
        print("შეკვეთების დამუშავება დაიწყო...")
        print("======================================")
        print()


        # ვიძახებთ ძირითად ფუნქციას
        # დაბრუნებულ შედეგს ვინახავთ result-ში
        result = func(orders)


        print()
        print("======================================")
        print("შეკვეთების დამუშავება დასრულდა.")
        print("======================================")
        print()


        # ====================================================
        # ვითვლით შეკვეთების რაოდენობას სტატუსების მიხედვით
        # ====================================================

        completed_count = len(result["completed_orders"])

        cancelled_count = len(result["cancelled_orders"])

        pending_count = len(result["pending_orders"])


        print(
            "დასრულებული შეკვეთების რაოდენობა:",
            completed_count
        )

        print(
            "გაუქმებული შეკვეთების რაოდენობა:",
            cancelled_count
        )

        print(
            "მოლოდინში მყოფი შეკვეთების რაოდენობა:",
            pending_count
        )

        print(
            "სრული შემოსავალი:",
            result["total_income"]
        )


        # ====================================================
        # მომხმარებლების დანახარჯები
        # ====================================================

        print()
        print("მომხმარებლების დანახარჯები:")

        customer_spending = result["customer_spending"]


        # თითოეულ მომხმარებელს ცალკე ვბეჭდავთ
        for customer in customer_spending:

            print(
                customer,
                "-",
                customer_spending[customer]
            )


        # ====================================================
        # ვპოულობთ მომხმარებელს,
        # რომელმაც ყველაზე მეტი თანხა დახარჯა
        # ====================================================

        max_customer = None

        max_spending = 0


        for customer in customer_spending:

            if customer_spending[customer] > max_spending:

                max_spending = customer_spending[customer]

                max_customer = customer


        print()

        if max_customer != None:

            print(
                "ყველაზე მეტი თანხა დახარჯა:",
                max_customer
            )

            print(
                "დახარჯული თანხა:",
                max_spending
            )

        else:

            print(
                "დასრულებული შეკვეთები არ არის."
            )


        # ====================================================
        # ვპოულობთ ყველაზე ძვირადღირებულ
        # დასრულებულ შეკვეთას
        # ====================================================

        most_expensive_order = None

        max_order_price = 0


        for order in result["completed_orders"]:

            # შეკვეთის სრული ფასი
            total_price = (
                order["price"] * order["quantity"]
            )


            if total_price > max_order_price:

                max_order_price = total_price

                most_expensive_order = order


        print()

        if most_expensive_order != None:

            print(
                "ყველაზე ძვირადღირებული "
                "დასრულებული შეკვეთა:"
            )

            print(
                "მომხმარებელი:",
                most_expensive_order["customer"]
            )

            print(
                "პროდუქტი:",
                most_expensive_order["product"]
            )

            print(
                "ერთი პროდუქტის ფასი:",
                most_expensive_order["price"]
            )

            print(
                "რაოდენობა:",
                most_expensive_order["quantity"]
            )

            print(
                "შეკვეთის სრული ფასი:",
                max_order_price
            )

        else:

            print(
                "დასრულებული შეკვეთა არ მოიძებნა."
            )


        return result


    return wrapper


# ============================================================
# ძირითადი შეკვეთების დამუშავების ფუნქცია
# ============================================================

@validate_orders
@execution_time
@analyze_orders
def process_orders(orders):


    # დასრულებული შეკვეთების სია
    completed_orders = []


    # გაუქმებული შეკვეთების სია
    cancelled_orders = []


    # მოლოდინში მყოფი შეკვეთების სია
    pending_orders = []


    # დასრულებული შეკვეთებიდან მიღებული სრული შემოსავალი
    total_income = 0


    # მომხმარებლების მიერ დახარჯული თანხები
    customer_spending = {}


    # ========================================================
    # გადავუყვებით ყველა შეკვეთას
    # ========================================================

    for order in orders:


        # ვითვლით კონკრეტული შეკვეთის სრულ ფასს
        total_price = (
            order["price"] * order["quantity"]
        )


        # მომხმარებლის სახელს ვინახავთ ცვლადში
        customer = order["customer"]


        # ====================================================
        # დასრულებული შეკვეთა
        # ====================================================

        if order["status"] == "completed":


            # დასრულებულ შეკვეთას ვამატებთ სიაში
            completed_orders.append(order)


            # შეკვეთის თანხას ვამატებთ საერთო შემოსავალს
            total_income = total_income + total_price


            # ვამოწმებთ მომხმარებელი უკვე არის თუ არა
            # customer_spending ლექსიკონში
            if customer in customer_spending:


                # თუ არის, ვუმატებთ ახალ თანხას
                customer_spending[customer] = (
                    customer_spending[customer]
                    + total_price
                )


            else:


                # თუ მომხმარებელი ჯერ არ არის,
                # ვქმნით ახალ ჩანაწერს
                customer_spending[customer] = (
                    total_price
                )


        # ====================================================
        # მოლოდინში მყოფი შეკვეთა
        # ====================================================

        elif order["status"] == "pending":


            # შეკვეთას ვამატებთ მოლოდინის სიაში
            pending_orders.append(order)


            print(
                "შეკვეთა მოლოდინშია:",
                order["customer"],
                "-",
                order["product"]
            )


        # ====================================================
        # გაუქმებული შეკვეთა
        # ====================================================

        elif order["status"] == "cancelled":


            # შეკვეთას ვამატებთ გაუქმებულ სიაში
            cancelled_orders.append(order)


            print(
                "შეკვეთა გაუქმებულია:",
                order["customer"],
                "-",
                order["product"]
            )


    # ========================================================
    # ვაბრუნებთ დამუშავებული შეკვეთების შედეგებს
    # ========================================================

    return {

        "completed_orders": completed_orders,

        "cancelled_orders": cancelled_orders,

        "pending_orders": pending_orders,

        "total_income": total_income,

        "customer_spending": customer_spending

    }


# ============================================================
# მომხმარებლისგან შეკვეთების ინფორმაციის მიღება
# ============================================================

def get_orders():


    # აქ შევინახავთ ყველა ახალ შეკვეთას
    orders = []


    # ========================================================
    # შეკვეთების რაოდენობის შეყვანა
    # ========================================================

    while True:

        try:

            order_count = int(
                input(
                    "შეიყვანეთ შეკვეთების რაოდენობა: "
                )
            )


            # შეკვეთების რაოდენობა
            # აუცილებლად უნდა იყოს 0-ზე მეტი
            if order_count <= 0:

                raise ValueError(
                    "შეკვეთების რაოდენობა "
                    "უნდა იყოს 0-ზე მეტი"
                )


            break


        except ValueError as error:

            print()
            print("შეცდომა:", error)


    # ========================================================
    # თითოეული შეკვეთის შეყვანა
    # ========================================================

    for i in range(order_count):


        print()
        print("======================================")
        print("შეკვეთა №", i + 1)
        print("======================================")


        # ====================================================
        # მომხმარებლის სახელი
        # ====================================================

        while True:

            customer = input(
                "შეიყვანეთ მომხმარებლის სახელი: "
            ).strip().title()


            # სახელი ცარიელი არ უნდა იყოს
            if customer == "":

                print()
                print(
                    "შეცდომა! "
                    "სახელი ცარიელი არ უნდა იყოს."
                )


            # სახელი არ უნდა შეიცავდეს ციფრებს
            elif any(
                character.isdigit()
                for character in customer
            ):

                print()
                print(
                    "შეცდომა! "
                    "სახელი არ უნდა შეიცავდეს ციფრებს."
                )


            else:

                break


        # ====================================================
        # პროდუქტის არჩევა
        # ====================================================

        while True:


            # გამყიდველს ვაჩვენებთ პროდუქტების სიას
            print()
            print("აირჩიეთ პროდუქტი:")
            print()
            print("1 - Laptop      - ფასი: 2500")
            print("2 - Mouse       - ფასი: 50")
            print("3 - Keyboard    - ფასი: 150")
            print("4 - Monitor     - ფასი: 800")
            print("5 - Headphones  - ფასი: 300")


            # გამყიდველი ირჩევს პროდუქტს ციფრით
            product_choice = input(
                "შეიყვანეთ 1, 2, 3, 4 ან 5: "
            ).strip()


            # ----------------------------------------------
            # Laptop
            # ----------------------------------------------

            if product_choice == "1":

                product = "Laptop"

                price = 2500

                break


            # ----------------------------------------------
            # Mouse
            # ----------------------------------------------

            elif product_choice == "2":

                product = "Mouse"

                price = 50

                break


            # ----------------------------------------------
            # Keyboard
            # ----------------------------------------------

            elif product_choice == "3":

                product = "Keyboard"

                price = 150

                break


            # ----------------------------------------------
            # Monitor
            # ----------------------------------------------

            elif product_choice == "4":

                product = "Monitor"

                price = 800

                break


            # ----------------------------------------------
            # Headphones
            # ----------------------------------------------

            elif product_choice == "5":

                product = "Headphones"

                price = 300

                break


            # ----------------------------------------------
            # არასწორი არჩევანი
            # ----------------------------------------------

            else:

                print()
                print(
                    "შეცდომა! "
                    "აირჩიეთ მხოლოდ 1, 2, 3, 4 ან 5."
                )


        # არჩეული პროდუქტის ინფორმაცია
        print()
        print("არჩეული პროდუქტი:", product)
        print("ერთი პროდუქტის ფასი:", price)


        # ====================================================
        # პროდუქტის რაოდენობა
        # ====================================================

        while True:

            try:

                quantity = int(
                    input(
                        "შეიყვანეთ პროდუქტის რაოდენობა: "
                    )
                )


                # რაოდენობა უნდა იყოს 0-ზე მეტი
                if quantity <= 0:

                    raise ValueError(
                        "რაოდენობა უნდა იყოს 0-ზე მეტი"
                    )


                break


            except ValueError:

                print()
                print(
                    "შეცდომა! რაოდენობა უნდა იყოს "
                    "დადებითი მთელი რიცხვი."
                )


        # ====================================================
        # შეკვეთის სრული ღირებულება
        # ====================================================

        total_price = price * quantity


        print()
        print(
            "შეკვეთის სრული ღირებულება:",
            total_price
        )


        # ====================================================
        # შეკვეთის სტატუსის არჩევა
        # ====================================================

        while True:


            # გამყიდველს ვაჩვენებთ სტატუსების მენიუს
            print()
            print("აირჩიეთ შეკვეთის სტატუსი:")
            print()
            print("1 - დასრულებული შეკვეთა")
            print("2 - მოლოდინში მყოფი შეკვეთა")
            print("3 - გაუქმებული შეკვეთა")


            # გამყიდველი ირჩევს სტატუსს ციფრით
            status_choice = input(
                "შეიყვანეთ 1, 2 ან 3: "
            ).strip()


            # ----------------------------------------------
            # დასრულებული
            # ----------------------------------------------

            if status_choice == "1":

                status = "completed"

                break


            # ----------------------------------------------
            # მოლოდინში
            # ----------------------------------------------

            elif status_choice == "2":

                status = "pending"

                break


            # ----------------------------------------------
            # გაუქმებული
            # ----------------------------------------------

            elif status_choice == "3":

                status = "cancelled"

                break


            # ----------------------------------------------
            # არასწორი არჩევანი
            # ----------------------------------------------

            else:

                print()
                print(
                    "შეცდომა! "
                    "აირჩიეთ მხოლოდ 1, 2 ან 3."
                )


        # ====================================================
        # ვქმნით ერთი შეკვეთის dictionary-ს
        # ====================================================

        order = {

            "customer": customer,

            "product": product,

            "price": price,

            "quantity": quantity,

            "status": status

        }


        # ====================================================
        # შეკვეთას ვამატებთ orders სიაში
        # ====================================================

        orders.append(order)


        print()
        print("--------------------------------------")
        print("შეკვეთა წარმატებით დაემატა.")
        print("--------------------------------------")

        print("მომხმარებელი:", customer)

        print("პროდუქტი:", product)

        print("ერთი პროდუქტის ფასი:", price)

        print("რაოდენობა:", quantity)

        print("სრული ღირებულება:", total_price)


        # სტატუსის ქართულად ჩვენება
        if status == "completed":

            print("სტატუსი: დასრულებული")


        elif status == "pending":

            print("სტატუსი: მოლოდინში")


        elif status == "cancelled":

            print("სტატუსი: გაუქმებული")


    # ========================================================
    # ყველა შეკვეთის შეყვანის შემდეგ
    # ვაბრუნებთ orders სიას
    # ========================================================

    return orders


# ============================================================
# პროგრამის გაშვება
# ============================================================

orders = get_orders()

process_orders(orders)