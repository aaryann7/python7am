
product = {'Apple':{'price': 10}, 'Mango' : {'price' :20}, 'Kiwi' :{'price' : 50}}

print("\n--- Available Items in the Store ---")
for item, details in product.items():
    print(f"{item}: Rs.{details['price']} per unit")



# Display cart 

def disp_cart(cart):
    if not cart:
        print("Cart is empty")
    print("Items in your cart")
    total = 0
    for items, details in cart.items():
        print(f"{items}: {details['price']} x {details['quantity']} = Rs.{details['price'] * details['quantity']}")
        total += details['price'] * details['quantity']
        print(f"Yout total is Rs.{total}")
    


# Add items in cart 

def add_item (cart):


    
    input_name = input("Enter the name of the product: ").capitalize()


# Check if it exists in products 

    if input_name in product:
        price = product[input_name]['price']
        quantity = int(input(f"How many {input_name}'s do you want? "))
    

    # Add or update cart 

        if input_name in cart:
            cart[input_name]['quantity'] += quantity
        else:
            cart[input_name] = {'price' :  price , 'quantity' : quantity}

        print(f"{quantity} {input_name}'s added to your cart")

    else:
        print(f"{input_name} is not available")

    
# Remove items 

def remove_item(cart):
    if not cart:
        print("There are no items in cart")

    disp_cart(cart)
    item_name = input("Enter the name of the product you want to remove")

    if item_name not in cart:
        print("This product is not in your cart")
    else:
        del cart[item_name]
        print(f"{item_name} is removed from your cart)")








def main():
    cart = {}

    while True:

        print("\nShopping cart menu")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart and total bill")
        print("4. Exit")
        

        choice = input("Select an option")

        if choice == '1':
            add_item(cart)
        elif choice == '2':
            remove_item(cart)
        elif choice == '3':
            disp_cart(cart)
        elif choice == '4':
            break
        else:
         print("Invalid Option")

    


main()
