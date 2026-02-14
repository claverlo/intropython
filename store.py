from catalog import catalog

# Global variable
cart = []

def print_header(text):
    print("--------------------------")
    print(text)
    print("--------------------------")

def print_menu():
    print("Menu")
    print(" 1.- View Catalog")
    print(" 2.- Search Product")
    print(" 3.- View Cart")
    # More features
    print(" 0.- Quit")

# Catalog and Cart Function
def print_catalog():
    print_header("- Our Catalog -")
    for prod in catalog:        # ljust means justify left. So 15 spaces to the right
        print(f' | {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')

    answer = input("Type ID to add (N to close): ")
    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)

    print("----------------")

    def add_product_to_cart(prod_id):
        found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)  # add product to the cart
            print(f'{prod["title"]} added to your cart.')
            break  # stops after finding product
    if not found:
        print("**Error: Invalid ID")
    print("--------------------------")

def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f' | {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')


# Main Program Loop
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to Story ab")
    print_menu()

    option = input("Choose an option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        print("Search Product")
    elif option == "3":
        view_cart()
    # Add Features
    elif option == "q" or option == "Q":
        print("Good Bye!")
        break
    else:
        print("** Error: invalid option")
        print("------------------------------\n")
