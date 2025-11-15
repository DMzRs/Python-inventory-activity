items = []
prices = {}

in_process = True

while in_process:
    print("========INVENTORY MENU========")
    print("[1] Add item")
    print("[2] Update price")
    print("[3] Exit")
    choice = input("Select an option: ")

    if choice == '1':
        item_name = input("Enter item name: ")

        if item_name in items:
            print(f"Item '{item_name}' already exists in inventory.")
            continue

        try:
            item_price = float(input("Enter item price: "))

            if item_price < 0:
                print("Price cannot be negative.")
                continue

            items.append(item_name)
            prices[item_name] = item_price
            print(f"Item '{item_name}' added with price {item_price}.")

        except ValueError:
            print("Invalid price. Please enter a numeric value.")
        
    elif choice == '2':
        item_name = input("Enter item name to update: ")

        if item_name in prices:
            
            try:
                new_price = float(input("Enter new price: "))

                if new_price < 0:
                    print("Price cannot be negative.")
                    continue

                prices[item_name] = new_price
                print(f"Price for '{item_name}' updated to {new_price}.")

            except ValueError:
                print("Invalid price. Please enter a numeric value.")
        else:
            print(f"Item '{item_name}' not found in inventory.")

    elif choice == '3':
        print("Exiting inventory menu....")
        in_process = False
        
    else:
        print("Invalid option. Please select a valid menu option.")

    