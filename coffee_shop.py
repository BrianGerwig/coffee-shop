def print_receipt(name, drink, size):
    print("==========================")
    print("   BRIAN'S COFFEE SHOP")
    print("==========================")
    print("Customer:", name)
    print("Drink:", drink)
    print("Size:", size)

print("Welcome to Brian's Coffee Shop!")

answer = "yes"

while answer == "yes":
    print("Coffee order started.")

    name = input("What is your name? ")
    drink = input("What drink would you like? ")
    size = input("What size would you like (small, medium, large)? ")

    if size == "large":
        print("$6.00")
    elif size == "medium":
        print("$5.00")
    elif size == "small":
        print("$4.00")
    else:
         print("Sorry, we don't have that size.")

    print_receipt(name, drink, size)
    answer = input("Would you like to take another order? (yes/no): ")

print("Thanks for visiting Brian's Coffee Shop!")