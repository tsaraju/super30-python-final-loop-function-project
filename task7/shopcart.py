'''
7 Shopping Cart

Create a simple cart where users can

add products
remove products
view cart
calculate bill
exit

The application should continue until Exit is selected.
'''
# Function to add a product
def add_product(cart):
    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(product)

    print(f"{name} added to cart successfully!")


# Function to remove a product
def remove_product(cart):
    name = input("Enter product name to remove: ")

    for product in cart:
        if product["name"].lower() == name.lower():
            cart.remove(product)
            print(f"{name} removed from cart.")
            return

    print("Product not found in cart.")


# Function to view the cart
def view_cart(cart):
    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    print("\n===== Shopping Cart =====")

    for product in cart:
        item_total = product["price"] * product["quantity"]

        print(f"Product: {product['name']}")
        print(f"Price: ₹{product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Total: ₹{item_total:.2f}")
        print("------------------------")


# Function to calculate the bill
def calculate_bill(cart):
    total = 0

    for product in cart:
        total += product["price"] * product["quantity"]

    print(f"\nTotal Bill: ₹{total:.2f}")


# Main function
def main():
    cart = []

    while True:
        print("\n===== Shopping Cart =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Calculate Bill")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_product(cart)

        elif choice == "2":
            remove_product(cart)

        elif choice == "3":
            view_cart(cart)

        elif choice == "4":
            calculate_bill(cart)

        elif choice == "5":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the application
main()

'''
Example Output
===== Shopping Cart =====
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Bill
5. Exit

Enter your choice (1-5): 1
Enter product name: Laptop
Enter product price: ₹50000
Enter quantity: 1
Laptop added to cart successfully!

Enter your choice (1-5): 1
Enter product name: Mouse
Enter product price: ₹500
Enter quantity: 2
Mouse added to cart successfully!

Enter your choice (1-5): 4

Total Bill: ₹51000.00

Enter your choice (1-5): 5
Thank you for shopping!

'''