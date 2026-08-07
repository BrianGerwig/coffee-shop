def get_customer_name():
    customer_name = input("What is your name? ")


    return customer_name

def get_drink():
    drink = input("What drink would you like? ").lower()
    while drink != "coffee" and drink != "tea" and drink != "chai":
        print("Invalid selection.")
        drink = input("What drink would you like? (coffee, tea or chai)").lower()

    return drink

def get_espresso():
    shot = input("Would you like to add a shot of espresso? (yes/no) ").lower()

    while shot != "yes" and shot != "no":
        print("Please answer yes or no.")
        shot = input("Would you like to add a shot of espresso? (yes/no) ").lower()

    if shot == "yes":
        return True
    else:
        return False


def get_size():
    size = input("What size would you like? ").lower()
    while size != "small" and size != "medium" and size != "large":
        print("Invalid size.")
        size = input("What size would you like? (small, medium or large)").lower()

    return size

def calculate_price(size, shot):

    if size == "large":
        price = 6
    elif size == "medium":
        price = 5
    elif size == "small":
        price = 4
    if shot:
        price = price + 2

    return price

def print_receipt(customer_name,drink,size,shot,price):
    print("==========================")
    print("   BRIAN'S COFFEE SHOP")
    print("==========================")
    print("Customer:", customer_name)
    print("Drink:", drink)
    print("Size:", size)

    if shot:
        shot_display = "Yes"
    else:
        shot_display = "No"

    print("Espresso shot:", shot_display)
    print(f"Price: ${price:.2f}")
        
def main():
    print("Welcome to Brian's Coffee Shop!")

    answer = "yes"

    while answer == "yes":
        customer_name = get_customer_name()
        drink = get_drink()
        size = get_size()
        shot = get_espresso()
        price = calculate_price(size,shot)

        print_receipt(customer_name,drink,size,shot,price)

        answer = input("Would you like to take another order? (yes/no): ").lower()

    print("Thanks for visiting Brian's Coffee Shop!")

main()