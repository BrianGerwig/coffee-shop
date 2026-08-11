def get_customer_name():
    customer_name = input("What is your name? ")


    return customer_name

def get_drink():
    drink = input("What drink would you like? ").lower()
    while drink != "coffee" and drink != "tea" and drink != "chai":
        print("Invalid selection.")
        drink = input("What drink would you like? (coffee, tea or chai)").lower()

    return drink

def get_temperature():
    temperature = input("Would you like your drink hot or iced? ").lower()
    while temperature != "hot" and temperature != "iced":
        print("Invalid selection.")
        temperature = input("Would you like your drink hot or iced? ").lower()

    return temperature

def get_milk():
    milk = input("What kind of milk would you like? (whole, oat or almond?) ").lower()

    while milk != "whole" and milk != "oat" and milk != "almond":
        print("Invalid selection.")
        milk = input("What milk would you like? (whole, oat or almond) ").lower()

    return milk

def get_espresso():
    shots = int(input("How many shots of espresso would you like? (0-3)"))

    while shots < 0 or shots > 3:
        print("Invalid selection.")
        shots = int(input("How many shots of espresso would you like? (0-3)"))

    return shots

def get_size():
    size = input("What size would you like? ").lower()
    while size != "small" and size != "medium" and size != "large":
        print("Invalid size.")
        size = input("What size would you like? (small, medium or large)").lower()

    return size

def calculate_price(size, shots):

    if size == "large":
        price = 6
    elif size == "medium":
        price = 5
    elif size == "small":
        price = 4

    price = price + shots * 2

    return price

def print_receipt(customer_name,drink,temperature,milk,size,shots,price):
    print("==========================")
    print("   BRIAN'S COFFEE SHOP")
    print("==========================")
    print("Customer:", customer_name)
    print("Drink:", temperature, drink)
    print("Milk:", milk)
    print("Size:", size)

    if shots == 1:
        print("Espresso shot:", shots)
    else:
        print("Espresso shots:", shots)

    print()

    print(f"Price: ${price:.2f}")
        
def main():
    print("Welcome to Brian's Coffee Shop!")

    answer = "yes"
    orders = []

    while answer == "yes":
        customer_name = get_customer_name()
        drink = get_drink()
        temperature = get_temperature()
        milk = get_milk()
        size = get_size()
        shots = get_espresso()
        price = calculate_price(size,shots)

        order = {
            "customer": customer_name,
            "drink": drink,
            "temperature": temperature,
            "milk": milk,
            "size": size,
            "shots": shots,
            "price": price,
        }
        orders.append(order)

        print_receipt(customer_name,drink,temperature,milk,size,shots,price)

        answer = input("Would you like to take another order? (yes/no): ").lower()

    print()
    print("ORDERS TODAY")
    print("------------")

    for order in orders:
        print(f'{order["customer"]} - {order["temperature"]} {order["drink"]} - {order["size"]} - ${order["price"]:.2f}')

    print("Total orders:", len(orders))
    print()
    print("Thanks for visiting Brian's Coffee Shop!")

main()