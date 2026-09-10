# =========================================
# დავალება 12
# Order Analysis + Decorator
# =========================================


# დეკორატორი
def analyze_orders(func):

    def wrapper(orders):

        # ფუნქციის შესრულებამდე
        print("Order processing started...")

        # ვიძახებთ ძირითად ფუნქციას
        # და ვინახავთ დაბრუნებულ შედეგს.
        result = func(orders)

        # ფუნქციის დასრულების შემდეგ
        print("Order processing finished.")

        # ვითვლით completed შეკვეთების რაოდენობას.
        completed_count = len(result["completed_orders"])

        # ვითვლით cancelled შეკვეთების რაოდენობას.
        cancelled_count = len(result["cancelled_orders"])

        # ვითვლით pending შეკვეთების რაოდენობას.
        pending_count = len(result["pending_orders"])

        print("Completed orders:", completed_count)
        print("Cancelled orders:", cancelled_count)
        print("Pending orders:", pending_count)

        # completed შეკვეთებიდან მიღებული სრული შემოსავალი.
        print("Total income:", result["total_income"])

        # თითოეული მომხმარებლის დახარჯული თანხა.
        print("Customer spending:", result["customer_spending"])

        # აუცილებლად ვაბრუნებთ შედეგს,
        # რათა დეკორირებულმა ფუნქციამაც დააბრუნოს dictionary.
        return result

    return wrapper


# =========================================
# შეკვეთების დამუშავების ფუნქცია
# =========================================

@analyze_orders
def process_orders(orders):

    # სხვადასხვა სტატუსის შეკვეთებისთვის
    # ვქმნით ცარიელ ლისტებს.
    completed_orders = []
    cancelled_orders = []
    pending_orders = []

    # completed შეკვეთებიდან მიღებული
    # სრული შემოსავალი.
    total_income = 0

    # აქ შევინახავთ თითოეული მომხმარებლის
    # მთლიან დანახარჯს.
    customer_spending = {}

    # სათითაოდ გადავუყვებით ყველა შეკვეთას.
    for order in orders:

        # ერთი შეკვეთის სრული ფასი:
        # პროდუქტის ფასი * რაოდენობა.
        total_price = order["price"] * order["quantity"]

        # თუ შეკვეთა completed არის.
        if order["status"] == "completed":

            completed_orders.append(order)

            # შემოსავალში ვამატებთ მხოლოდ completed შეკვეთებს.
            total_income = total_income + total_price

            customer = order["customer"]

            # თუ მომხმარებელი უკვე არის dictionary-ში,
            # მის ძველ დანახარჯს ვუმატებთ ახალ თანხას.
            if customer in customer_spending:
                customer_spending[customer] = (
                    customer_spending[customer] + total_price
                )

            # თუ მომხმარებელი ჯერ არ არის dictionary-ში,
            # პირველად ვამატებთ.
            else:
                customer_spending[customer] = total_price

        # თუ შეკვეთა pending არის.
        elif order["status"] == "pending":
            pending_orders.append(order)

        # თუ შეკვეთა cancelled არის.
        elif order["status"] == "cancelled":
            cancelled_orders.append(order)

    # საბოლოოდ ფუნქცია აბრუნებს dictionary-ს.
    return {
        "completed_orders": completed_orders,
        "cancelled_orders": cancelled_orders,
        "pending_orders": pending_orders,
        "total_income": total_income,
        "customer_spending": customer_spending
    }


# =========================================
# მონაცემები
# =========================================

orders = [
    {
        "customer": "Ani",
        "product": "Laptop",
        "price": 2000,
        "quantity": 1,
        "status": "completed"
    },

    {
        "customer": "Luka",
        "product": "Mouse",
        "price": 50,
        "quantity": 2,
        "status": "pending"
    },

    {
        "customer": "Ani",
        "product": "Keyboard",
        "price": 100,
        "quantity": 2,
        "status": "completed"
    },

    {
        "customer": "Nika",
        "product": "Monitor",
        "price": 500,
        "quantity": 1,
        "status": "cancelled"
    },

    {
        "customer": "Luka",
        "product": "Phone",
        "price": 1000,
        "quantity": 1,
        "status": "completed"
    }
]


# ფუნქციის გამოძახება
result = process_orders(orders)