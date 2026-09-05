'''
3 Inventory Management

Maintain products containing

product name
price
quantity
Provide functions to
add product
display products
search product
update quantity
calculate total inventory value
'''

# Function to add a product
def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter product quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Product added successfully!")


# Function to display all products
def display_products(products):
    if len(products) == 0:
        print("No products available.")
        return

    print("\n----- Product List -----")

    for product in products:
        print(f"Name: {product['name']}")
        print(f"Price: ₹{product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print("------------------------")


# Function to search for a product
def search_product(products):
    name = input("Enter product name to search: ")

    for product in products:
        if product["name"].lower() == name.lower():
            print("\nProduct found!")
            print(f"Name: {product['name']}")
            print(f"Price: ₹{product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")
            return

    print("Product not found.")


# Function to update product quantity
def update_quantity(products):
    name = input("Enter product name: ")

    for product in products:
        if product["name"].lower() == name.lower():
            quantity = int(input("Enter new quantity: "))
            product["quantity"] = quantity
            print("Quantity updated successfully!")
            return

    print("Product not found.")


# Function to calculate total inventory value
def calculate_inventory_value(products):
    total = 0

    for product in products:
        total += product["price"] * product["quantity"]

    return total


# Main function
def main():
    products = []

    while True:
        print("\n===== Inventory Management =====")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Update Quantity")
        print("5. Calculate Total Inventory Value")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_product(products)

        elif choice == "2":
            display_products(products)

        elif choice == "3":
            search_product(products)

        elif choice == "4":
            update_quantity(products)

        elif choice == "5":
            total = calculate_inventory_value(products)
            print(f"Total Inventory Value: ₹{total:.2f}")

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()

'''
Example Output
Name: Laptop
Price: ₹50000
Quantity: 2

Name: Mouse
Price: ₹500
Quantity: 5

Total Inventory Value: ₹102500.00

'''