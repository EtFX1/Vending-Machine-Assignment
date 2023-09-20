vending_machine_info = {

    #! item_code: [item_name, item_price]
    "A1": ["Crisps (type 1)", 0.50],
    "A2": ["Crisps (type 2)", 0.50],
    "B1": ["Chocolate (type 1)", 0.75],
    "B2": ["Chocolate (type 2)", 0.75],
    "C1": ["Sweets (type 1)", 0.40],
    "C2": ["Sweets (type 2)", 0.60],
    "D1": ["Sandwich (type 1)", 1.20],
    "D2": ["Sandwich (type 2)", 1.40],
    "E1": ["Drink (type 1)", 0.95],
    "E2": ["Drink (type 2)", 1.50]
}

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
            item_info = vending_machine_info
            [user_item_code_input]

            item_name = item_info[0]
            item_price = item_info[1]

        # * error handling by checking to see if "user_item_code_input" is a key in the dictionary

        except KeyError:
            print("Item does not exist, check item code")
            print()
            continue

        print(f"{item_name}: £{item_price}")

        break


print(handleItemCode())
