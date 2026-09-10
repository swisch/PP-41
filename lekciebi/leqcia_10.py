# argumentis tipebi 

# positional, default, keyword
# *args, **kwargs

# def math_operation(a, b):
#     return a // b 
# print(math_operation(4, 5)) # positional arguments

# def math_operation(a, b):
#     return a // b 
# print(math_operation(b=7, a=5)) # keyword arguments

# def default_argument(a, name="ani"):
#     print("Greet",a,  name)

# default_argument("A")
# default_argument("rame", "gadaawers") # default arguments


# *args
# *args - variable_length arguments 

# def total(*numbers):
#     print(sum(numbers))

# total(1, 2)
# total(5, 6, 7)
# total(4, 6, 1, 3, 4)



# **kwargs - keyword variable-length arguments
# dictii = dict(name='G', age="45")
# print(dictii)

# def display_data(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# display_data(name="ani", city='TB')


# # --------------------------------------------------------------------------------------

# def mix_args_kwargs(*args, **kwargs):
#     print("Positional Arguments", args)
#     print("Keyword arguments", kwargs)

# mix_args_kwargs(1, 2, 3, 4, 77, data="info", info="details")

# ---------------------------------------------------------------------------

# calculate_total_price(discount=60, tax=10)

def calculate_total_price(*args, **kwargs):
    total_price = sum(args) # args iqneba listi fasebis

    discount = kwargs.get('discount', 0) # {"key":"value"}
    total_price -= discount
    # total_price = total_price - discount

    tax_rate = kwargs.get('tax', 0)
    total_price += total_price * (tax_rate / 10)

    return total_price

def main():
    item_prices = [34, 65, 8]

    total = calculate_total_price(*item_prices, discount=50, tax=10)
    print("total price with discount and tax", total)

    total_2 = calculate_total_price(*item_prices)
    print("total price with NO discount and NO tax", total_2)

# main()

if __name__ == "__main__":
    main()


