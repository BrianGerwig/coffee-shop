def get_customer_name():
    customer_name = input("What is your name? ")

    return customer_name

def get_drink():
    drink = input("What drink would you like? ").lower()
    while drink != "coffee" and drink != "tea" and drink != "chai":
        print("Invalid selection.")
        drink = input("What drink would you like? (coffee, tea or chai)").lower()

    return drink

def get_size():
    size = input("What size would you like? ").lower()
    while size != "small" and size != "medium" and size != "large":
        print("Invalid size.")
        size = input("What size would you like? (small, medium or large)").lower()

    return size

def calculate_price(size):

    if size == "large":
        return 6
    elif size == "medium":
        return 5
    elif size == "small":
        return 4

def print_receipt(customer_name, drink, size, price):
    print("==========================")
    print("   BRIAN'S COFFEE SHOP")
    print("==========================")
    print("Customer:", customer_name)
    print("Drink:", drink)
    print("Size:", size)
    print("Price:", price)

def main():
    print("Welcome to Brian's Coffee Shop!")

    answer = "yes"

    while answer == "yes":
        customer_name = get_customer_name()
        drink = get_drink()
        size = get_size()
        price = calculate_price(size)

        print_receipt(customer_name,drink,size,price)

        answer = input("Would you like to take another order? (yes/no): ").lower()

    print("Thanks for visiting Brian's Coffee Shop!")

main()