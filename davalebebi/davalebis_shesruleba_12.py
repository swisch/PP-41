import time


# ============================================================
# შეკვეთების შემოწმების დეკორატორი
# ============================================================

def validate_orders(func):

    def wrapper(orders):

        try:

            # შეკვეთების სია არ უნდა იყოს ცარიელი
            if len(orders) == 0:
                raise ValueError(
                    "შეკვეთების სია ცარიელია"
                )


            # გადავუყვებით ყველა შეკვეთას
            for order in orders:

                # მომხმარებლის სახელი არ უნდა იყოს ცარიელი
                if order["customer"] == "":
                    raise ValueError(
                        "მომხმარებლის სახელი ცარიელია"
                    )


                # ფასი უნდა იყოს 0-ზე მეტი
                if order["price"] <= 0:
                    raise ValueError(
                        "ფასი უნდა იყოს 0-ზე მეტი"
                    )


                # რაოდენობა უნდა იყოს 0-ზე მეტი
                if order["quantity"] <= 0:
                    raise ValueError(
                        "რაოდენობა უნდა იყოს 0-ზე მეტი"
                    )


        except ValueError as error:

            print()
            print("შეკვეთების შემოწმების შეცდომა!")
            print("შეცდომა:", error)

            return


        # თუ მონაცემები სწორია,
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
        print(
            "პროგრამის შესრულების დრო:",
            total_time
        )


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
        result = func(orders)


        print()
        print("======================================")
        print("შეკვეთების დამუშავება დასრულდა.")
        print("======================================")
        print()


        # ====================================================
        # შეკვეთების რაოდენობა სტატუსების მიხედვით
        # ====================================================

        completed_count = len(
            result["completed_orders"]
        )

        cancelled_count = len(
            result["cancelled_orders"]
        )

        pending_count = len(
            result["pending_orders"]
        )


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

        customer_spending = result[
            "customer_spending"
        ]


        print()
        print("მომხმარებლების დანახარჯები:")


        for customer in customer_spending:

            print(
                customer,
                "-",
                customer_spending[customer]
            )


        # ====================================================
        # მომხმარებელი, რომელმაც ყველაზე მეტი თანხა დახარჯა
        # ====================================================

        max_customer = None
        max_spending = 0


        for customer in customer_spending:

            if (
                customer_spending[customer]
                > max_spending
            ):

                max_spending = (
                    customer_spending[customer]
                )

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
        # ყველაზე ძვირადღირებული დასრულებული შეკვეთა
        # ====================================================

        most_expensive_order = None
        max_order_price = 0


        for order in result["completed_orders"]:

            total_price = (
                order["price"]
                * order["quantity"]
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


    # დასრულებული შეკვეთები
    completed_orders = []


    # გაუქმებული შეკვეთები
    cancelled_orders = []


    # მოლოდინში მყოფი შეკვეთები
    pending_orders = []


    # საერთო შემოსავალი
    total_income = 0


    # მომხმარებლების დანახარჯები
    customer_spending = {}


    # გადავუყვებით ყველა შეკვეთას
    for order in orders:


        # შეკვეთის სრული ფასი
        total_price = (
            order["price"]
            * order["quantity"]
        )


        customer = order["customer"]


        # ====================================================
        # დასრულებული შეკვეთა
        # ====================================================

        if order["status"] == "completed":


            completed_orders.append(order)


            total_income = (
                total_income
                + total_price
            )


            # თუ მომხმარებელი უკვე არსებობს ლექსიკონში,
            # მის თანხას ვუმატებთ ახალ შეკვეთას
            if customer in customer_spending:

                customer_spending[customer] = (
                    customer_spending[customer]
                    + total_price
                )


            # თუ მომხმარებელი ჯერ არ არსებობს,
            # ვქმნით ახალ ჩანაწერს
            else:

                customer_spending[customer] = (
                    total_price
                )


        # ====================================================
        # მოლოდინში მყოფი შეკვეთა
        # ====================================================

        elif order["status"] == "pending":


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


            cancelled_orders.append(order)


            print(
                "შეკვეთა გაუქმებულია:",
                order["customer"],
                "-",
                order["product"]
            )


    # ვაბრუნებთ დამუშავებულ ინფორმაციას
    return {

        "completed_orders":
            completed_orders,

        "cancelled_orders":
            cancelled_orders,

        "pending_orders":
            pending_orders,

        "total_income":
            total_income,

        "customer_spending":
            customer_spending
    }


# ============================================================
# შეკვეთების ინფორმაციის შეყვანა
# ============================================================

def get_orders():


    # აქ შევინახავთ ყველა შეკვეთას
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


            if order_count <= 0:

                raise ValueError(
                    "შეკვეთების რაოდენობა "
                    "უნდა იყოს 0-ზე მეტი"
                )


            break


        except ValueError:

            print()
            print(
                "შეცდომა! შეიყვანეთ "
                "დადებითი მთელი რიცხვი."
            )


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


            if customer == "":

                print()
                print(
                    "შეცდომა! სახელი ცარიელი "
                    "არ უნდა იყოს."
                )


            elif any(
                character.isdigit()
                for character in customer
            ):

                print()
                print(
                    "შეცდომა! სახელი არ უნდა "
                    "შეიცავდეს ციფრებს."
                )


            else:

                break


        # ====================================================
        # პროდუქტის არჩევა
        # ====================================================

        while True:


            print()
            print("აირჩიეთ პროდუქტი:")
            print()
            print("1 - Laptop      - ფასი: 2500")
            print("2 - Mouse       - ფასი: 50")
            print("3 - Keyboard    - ფასი: 150")
            print("4 - Monitor     - ფასი: 800")
            print("5 - Headphones  - ფასი: 300")


            product_choice = input(
                "შეიყვანეთ 1, 2, 3, 4 ან 5: "
            ).strip()


            if product_choice == "1":

                product = "Laptop"
                price = 2500

                break


            elif product_choice == "2":

                product = "Mouse"
                price = 50

                break


            elif product_choice == "3":

                product = "Keyboard"
                price = 150

                break


            elif product_choice == "4":

                product = "Monitor"
                price = 800

                break


            elif product_choice == "5":

                product = "Headphones"
                price = 300

                break


            else:

                print()
                print(
                    "შეცდომა! აირჩიეთ მხოლოდ "
                    "1, 2, 3, 4 ან 5."
                )


        # არჩეული პროდუქტის ჩვენება
        print()
        print(
            "არჩეული პროდუქტი:",
            product
        )

        print(
            "ერთი პროდუქტის ფასი:",
            price
        )


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


                if quantity <= 0:

                    raise ValueError(
                        "რაოდენობა უნდა იყოს "
                        "0-ზე მეტი"
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

        total_price = (
            price * quantity
        )


        print()
        print(
            "შეკვეთის სრული ღირებულება:",
            total_price
        )


        # ====================================================
        # შეკვეთის სტატუსის არჩევა
        # ====================================================

        while True:


            print()
            print("აირჩიეთ შეკვეთის სტატუსი:")
            print()
            print("1 - დასრულებული შეკვეთა")
            print("2 - მოლოდინში მყოფი შეკვეთა")
            print("3 - გაუქმებული შეკვეთა")


            status_choice = input(
                "შეიყვანეთ 1, 2 ან 3: "
            ).strip()


            if status_choice == "1":

                status = "completed"

                break


            elif status_choice == "2":

                status = "pending"

                break


            elif status_choice == "3":

                status = "cancelled"

                break


            else:

                print()
                print(
                    "შეცდომა! აირჩიეთ მხოლოდ "
                    "1, 2 ან 3."
                )


        # ====================================================
        # ვქმნით შეკვეთის dictionary-ს
        # ====================================================

        order = {

            "customer": customer,

            "product": product,

            "price": price,

            "quantity": quantity,

            "status": status
        }


        # შეკვეთას ვამატებთ სიაში
        orders.append(order)


        # ====================================================
        # დამატებული შეკვეთის ინფორმაცია
        # ====================================================

        print()
        print("--------------------------------------")
        print("შეკვეთა წარმატებით დაემატა.")
        print("--------------------------------------")


        print(
            "მომხმარებელი:",
            customer
        )

        print(
            "პროდუქტი:",
            product
        )

        print(
            "ერთი პროდუქტის ფასი:",
            price
        )

        print(
            "რაოდენობა:",
            quantity
        )

        print(
            "სრული ღირებულება:",
            total_price
        )


        # სტატუსის ქართულად ჩვენება
        if status == "completed":

            print(
                "სტატუსი: დასრულებული"
            )


        elif status == "pending":

            print(
                "სტატუსი: მოლოდინში"
            )


        elif status == "cancelled":

            print(
                "სტატუსი: გაუქმებული"
            )


    # ვაბრუნებთ ყველა შეკვეთას
    return orders


# ============================================================
# პროგრამის გაშვება
# ============================================================

orders = get_orders()

process_orders(orders)