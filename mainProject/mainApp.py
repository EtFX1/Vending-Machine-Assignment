vending_machine_info = {

    #! item_code: [item_name, item_price]
    "A1": ["Walkers (Ready Salted)", 0.50],
    "A2": ["Walkers (Bacon Flavoured)", 0.50],
    "B1": ["Snickers", 0.75],
    "B2": ["Twix", 0.75],
    "C1": ["Haribo (Starmix)", 0.40],
    "C2": ["Skittles", 0.60],
    "D1": ["Sandwich (Chicken & Bacon)", 1.20],
    "D2": ["Sandwich (BLT)", 1.40],
    "E1": ["Drink (Coca Cola)", 0.95],
    "E2": ["Drink (Fanta)", 1.50]
}

# todo: make this thing like.... not ugly
print(vending_machine_info)
print()


#! function to handle collecting user input
def handleItemCode():

    while True:

        try:
            # * user input's a vending machine code
            user_item_code_input = input("Type in item code: ").upper()
            print()

            # * mapping the user's input to the correct item in the dictionary
            item_info = vending_machine_info[user_item_code_input]

            item_name = item_info[0]
            item_price = item_info[1]

        # * error handling by checking to see if "user_item_code_input" is a key in the dictionary

        except KeyError:
            print("Item does not exist, check item code")
            print()
            continue

        # * displaying the item name and its price to the user
        print(f"{item_name}: £{item_price}p")
        print()

        break

    # * calling the handlePrice function
    return (handlePayment(item_name, item_price))


#! function to handle user payment
def handlePayment(item_name, item_price):

    while True:

        try:
            user_pay = float(input("Pay for your item: £"))
            print()

        # * error handling to catch an instance of the user entering a non numeric value
        except ValueError:
            print("Please enter a price")
            print()
            continue

        # * handling the price
        balance = round(item_price - user_pay, 1)

        #! checking whether the user has paid more or less than what is required

        # * tells the user how short they are if they've paid less
        if user_pay < item_price:
            print(f"You're £{balance} short ")
            print()

            # todo: add a way to "pay the rest"
            continue

        # * returns the user's change if they've paid more
        elif user_pay > item_price:
            print(f"Your change is £{abs(balance)} ")
            print()

        # * if they've provided the exact amount
        else:
            print("Exact amount paid. You're good to go!")
            print()

        break

    # * closing remark
    return (f"Enjoy your {item_name}!")


print(handleItemCode())
