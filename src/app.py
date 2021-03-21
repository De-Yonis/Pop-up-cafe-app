from datetime import datetime
from file_handlers import txt as mf
import os
def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


products = []
couriers = []

product_txt_path = "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/src/file_handlers/txt_files/list_of_products.txt"
couriers_txt_path = "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/src/file_handlers/txt_files/list_of_couriers.txt"


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


orders_list = [
    {
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "courier": 2,
        "status": "Preparing"
    }
]


def print_divider():
    print(80 * "-")


def update_product_list(product_to_update):
    new_product = input("\nWhat product would you like to replace this with: ")
    new_product = new_product.title()
    for prodct in range(0, len(products)):
        if product_to_update in products[prodct]:
            products[prodct] = new_product
            print("\nUpdated List:{}".format(products))


def update_courier_list(courier_to_update):
    new_courier = input(
        "\nEnter new name of courier: ")
    new_courier = new_courier.title()
    for cour in range(0, len(couriers)):
        if courier_to_update in couriers[cour]:
            couriers[cour] = new_courier
            print("\nUpdated List:{}".format(couriers))


def main_menu():
    print_divider()
    print("                           Welcome to 'MUNCH' cafe  ")
    print("\n")
    print("Please choose from the list below: \n \
    0. QUIT: \n \
    1. PRODUCT MENU: \n \
    2. COURIER MENU: \n \
    3. ORDER MENU: \n \
    ")
    select = int(input("Select your choice '0, 1, 2, 3': \n "))
    print_divider()
    if select == 0:
        print("Thank you for using the APP! See you next time.\nBye.")
        exit()

    if select == 1:
        product_menu()

    if select == 2:
        couriers_menu()

    if select == 3:
        order_menu()

    else:
        print("INVALID INPUT")
        main_menu()


def product_menu():
    print("")
    print("                                   PRODUCTS ")
    print_divider()
    print("Please choose from the list below: \n \
    0. MAIN MENU \n \
    1. PRINT PRODUCTS \n \
    2. ADD NEW PRODUCT \n \
    3. UPDATE PRODUCT \n \
    4. DELETE PRODUCT \n \
    ")
    product_selected = int(input("Select your choice '0, 1, 2, 3, 4':\n"))
    print('')

    if product_selected == 0:
        main_menu()

    if product_selected == 1:
        print(products)
        print("")
        print(("Products List: {}").format(products))
        print("")
        print_divider()

    if product_selected == 2:
        added_product = input("Please enter the name of new product: ")
        products.append(added_product.title())
        str_new_prod_list = "\n".join(products)
        print("\nNew Product List: \n\n{}".format(str_new_prod_list))
        print("")
        print_divider()

    if product_selected == 3:
        print("")
        print(products)
        valid_input = False
        while not valid_input:
            try:
                update_product = input(
                    "\nPlease select product you would like to update: ")
                update_product = update_product.title()

                if update_product in products:
                    valid_input = True
                else:
                    print(("\n{} is not in the product list").format(update_product))
            except:
                continue

        cancel_update_prod = int(input(
            (("\nAre you sure you want to update {} from the list?\n\n1 to continue or 0 to Cancel: ").format(update_product))))

        if cancel_update_prod == 0:
            print("\nCancelled")
            print_divider()

        elif cancel_update_prod == 1:
            update_product_list(update_product)
            print_divider()

        else:
            print("\nInvalid Input")
            print_divider()

    if product_selected == 4:
        print("")
        print(products)
        print("")
        valid_input3 = False
        while not valid_input3:
            try:
                removed_product = input(
                    "\nWhich product would you like to remove from the list above: ")

                removed_product = removed_product.title()

                if removed_product in products:
                    valid_input3 = True
                else:
                    print(("\n'{}' doesn't exist in the products list").format(
                        removed_product))
            except:
                continue

        cancel_remove_prod = int(input(
            (("\nAre you sure you want to remove {} from the list?\n\n1 to continue or 0 to Cancel: ").format(removed_product))))
        if cancel_remove_prod == 0:
            print("\nCancelled")
            print_divider()

        elif cancel_remove_prod == 1:
            products.remove(removed_product)
            print("\nNew List:{}".format(products))
            print("")
            print_divider()

        else:
            print("\nInvalid Input")
            print_divider()

    mf.save_data_intxt(product_txt_path, products)
    print("You have been redirected to the product menu")
    print_divider()
    product_menu()


def couriers_menu():
    print("")
    print("                                 COURIERS ")
    print_divider()
    print("Please choose from the list below: \n \
    0. MAIN MENU \n \
    1. PRINT COURIERS \n \
    2. ADD A NEW COURIER \n \
    3. UPDATE COURIER \n \
    4. DELETE COURIER \n \
    ")
    couriers_selected = int(input("Select your choice '0, 1, 2, 3, 4': \n "))
    print_divider()
    if couriers_selected == 0:
        main_menu()

    if couriers_selected == 1:
        print("")
        print(("Courier List: {}").format(couriers))
        print("")
        print_divider()

    if couriers_selected == 2:
        added_courier = input("Please enter the name of new courier: ")
        couriers.append(added_courier.title())
        str_new_cour_list = "\n".join(couriers)
        print("\nNew Couriers List: \n\n{}".format(str_new_cour_list))
        print("")
        print_divider()

    if couriers_selected == 3:
        print("")
        print(couriers)
        valid_input2 = False
        while not valid_input2:
            try:
                update_courier = input(
                    "\nPlease select courier you would like to update: ")
                update_courier = update_courier.title()

                if update_courier in couriers:
                    valid_input2 = True
                else:
                    print(("\n{} is not in the courier list").format(update_courier))
            except:
                continue

        cancel_update_couriers = int(input(
            (("\nAre you sure you want to update {} from the list?\n\n1 to continue or 0 to Cancel: ").format(update_courier))))

        if cancel_update_couriers == 0:
            print("\nCancelled")
            print_divider()

        elif cancel_update_couriers == 1:
            update_courier_list(update_courier)
            print_divider()

        else:
            print("\nInvalid Input")
            print_divider()

    if couriers_selected == 4:
        print("")
        print(couriers)
        print("")
        valid_input3 = False
        while not valid_input3:
            try:
                removed_courier = input(
                    "\nWhich courier would you like to remove from the list above: ")

                removed_courier = removed_courier.title()

                if removed_courier in couriers:
                    valid_input3 = True
                else:
                    print(("\nThe name '{}' doesn't exist in the couriers list").format(
                        removed_courier))
            except:
                continue

        cancel_remove_cour = int(input(
            (("\nAre you sure you want to remove {} from the list?\n\n1 to continue or 0 to Cancel: ").format(
                removed_courier))))
        if cancel_remove_cour == 0:
            print("\nCancelled")
            print_divider()

        elif cancel_remove_cour == 1:
            couriers.remove(removed_courier)
            print("\nNew List:{}".format(couriers))
            print("")
            print_divider()

        else:
            print("\nInvalid Input")
            print_divider()

    mf.save_data_intxt(couriers_txt_path, couriers)
    print("You have been redirected to the couriers menu ")
    print_divider()
    couriers_menu()


def order_menu():
    print("")
    print("                                   ORDERS ")
    print_divider()
    print("Please choose from the list below: \n \
    0. MAIN MENU \n \
    1. PRINT ORDERS \n \
    2. ADD NEW ORDER \n \
    3. UPDATE ORDER STATUS \n \
    4. UPDATE ORDER \n \
    5. DELETE ORDER \n \
    ")
    order_selected = int(input("Select your choice '0, 1, 2, 3, 4, 5':\n"))
    print('')

    if order_selected == 0:
        main_menu()

    if order_selected == 1:
        n = 1
        for dic in orders_list:
            print(((color.BOLD + color.UNDERLINE + color.RED +
                    "Order {}" + color.END)).format(n))
            n += 1
            for key, value in dic.items():
                print(("{}: {}").format(key, value))
            print("\n")

        print("")
        print("Task completed \n")
        print("You have been redirected to the Order menu")
        print_divider()
        order_menu()

    if order_selected == 2:
        while (True):
            name = input("Give the name of the customer you want to add: ")
            address = input("\nAddress of customer: ")
            phone = int(input("\nEnter the phone number: "))

            print(
                "\nChoose the number that matches the courier you would like to choose \n")

            for i, courier in enumerate(couriers, start=1):
                print(("Courier{} : {}").format(i, courier))
            courier_index = int(
                input("\nCourier: "))

            if courier_index == 0:
                print("\nINVALID INPUT")
                break

            orders_list.append({
                "customer_name": name.capitalize(),
                "customer_address": address,
                "customer_phone": phone,
                "courier": courier_index,
                "status": "Preparing"

            })

            cont = input("Want to add another? (Y/N): \n")
            if cont.capitalize() == "N":
                break

    if order_selected == 3:
        for i, orderdict in enumerate(orders_list, start=1):
            print(("Order {} | {}").format(i, orderdict))
        order_index = int(
            input("\nSelect a order to update or 0 to cancel: \n"))
        if order_index == 0:
            order_menu()
        else:
            chosen_dict = (orders_list[order_index - 1])
            new_status = input(
                "\nType a new status: 1)Preparing 2)Ready 3)Delivered: ")
            chosen_dict['status'] = new_status.capitalize()
            print_divider()
            print("The status of the order has now changed \n")
            print(chosen_dict)
            order_menu()

    if order_selected == 4:
        for i, orderdict in enumerate(orders_list, start=1):
            print(("Order {} | {}").format(i, orderdict))
        order_index = int(
            input("\nSelect a order to update or 0 to cancel: \n"))
        if order_index == 0:
            order_menu()

        chosen_dict = (orders_list[order_index - 1])

        new_name = input(
            "Update name or leave blank to skip: ")
        if new_name == "":
            print("\nSkipped")
        else:
            chosen_dict["customer_name"] = new_name.capitalize()
            print_divider()
            print("The name for this order has now changed \n")

        new_address = input("Update address or leave blank to skip: ")
        if new_address == "":
            print("\nSkipped")
        elif new_address != " ":
            chosen_dict["customer_address"] = new_address.capitalize()
            print_divider()
            print("The address for this order has now changed \n")

        new_phone = input("Update number or leave blank to skip: ")
        if new_phone == "":
            print("\nSkipped")
        elif new_phone != " ":
            chosen_dict["customer_phone"] = new_phone
            print_divider()
            print("The number for this order has now changed \n")

        new_courier = input("Update courier or leave blank to skip: ")
        if new_courier == "":
            print("\nSkipped")
        elif new_courier != " ":
            chosen_dict["courier"] = new_courier
            print_divider()
            print("The courier for this order has now changed \n")

        updated_status = input("Update status or leave blank to skip: ")
        if updated_status == "":
            print("\nSkipped")
        elif updated_status != "":
            chosen_dict['status'] = updated_status.capitalize()
            print_divider()
            print("The status for this order has now changed \n")

        print(("Order | {}").format(chosen_dict))

    if order_selected == 5:
        for i, orderdict in enumerate(orders_list, start=1):
            print(("Order {} | {}").format(i, orderdict))
        order_index = int(
            input("\nSelect an order to delete or 0 to cancel: \n"))

        if order_index == 0:
            print("Cancelled")
            order_menu()
        chosen_dict = (orders_list[order_index - 1])
        orders_list.remove(chosen_dict)
        print("The order has successfully been removed")
        order_menu()

    else:
        order_menu()


def greetings():
    now = datetime.now()

    ### Date formatting ####
    # %y/%Y - Year  %a/%A - Weekday  %b/%B - Month  %d/%D - Day of month
    print(now.strftime("%a, %d %b %y"))

    ### Time formatting ####
    # %I/H - 12/24 hour clock   %M - minute   $S - second  %p - AM or PM
    print(now.strftime("%I:%M:%S %p"))

    print_divider()
    name = input("Enter your name: ")
    print_divider()
    name = name.upper()
    print("                                HELLO {} \n ".format(name))
    mf.load_data_intxt(product_txt_path, products)
    mf.load_data_intxt(couriers_txt_path, couriers)


greetings()
main_menu()
