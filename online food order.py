
menu = {
    "Pizza": 250,
    "Burger": 150,
    "Biryani": 200,
    "Pasta": 180,
    "Sandwich": 100
    }

cart = []


def display_menu():
    print("\n----- FOOD MENU -----")

    for item, price in menu.items():
        print(item, "- ₹", price)


def add_to_cart(item, quantity):
    if item in menu:
        price = menu[item]
        total = price * quantity

        cart.append([item, quantity, total])

        print(item, "added to cart.")
        return total

    else:
        print("Item not available.")
        return 0


def calculate_bill():
    total = 0

    for order in cart:
        total = total + order[2]

    return total


def apply_discount(total):
    if total >= 500:
        discount = total * 0.10
    elif total >= 300:
        discount = total * 0.05
    else:
        discount = 0

    return discount


print("Welcome to  Food Corner!")

while True:

    display_menu()

    item = input("\nEnter the food item: ").title()

    quantity = int(input("Enter quantity: "))

    add_to_cart(item, quantity)

    choice = input("Do you want to order another item? (yes/no): ").lower()

    if choice == "no":
        break

print("\n----- YOUR ORDER -----")

for order in cart:
    print(
        order[0],
        "x",
        order[1],
        "= ₹",
        order[2]
    )

subtotal = calculate_bill()

discount = apply_discount(subtotal)

final_amount = subtotal - discount

print("\nSubtotal: ₹", subtotal)
print("Discount: ₹", discount)
print("Final Amount: ₹", final_amount)

print("\nThank you for ordering!")