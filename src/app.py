from datetime import datetime
# from file_handlers import txt as mf
from file_handlers import csv as imf
import os
import csv
def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
now = datetime.now()

products_list = []
couriers_list = []
orders_list = []
order_products = [] 

orders_csv_path = "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/src/file_handlers/csv_files/orders.csv"
couriers_csv_path = "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/src/file_handlers/csv_files/couriers.csv"
products_csv_path =  "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/src/file_handlers/csv_files/products.csv"

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

def get_name():
    name = input("What's your name?: ")
    return name

def create_greeting(name):
    print("                                HELLO,", name)

def print_greeting():
    name = get_name()
    create_greeting(name)

def print_divider():
    print(80 * "-")

def left_blank():
    print("\nYou have skipped this option")

def creating_new_product():
            while True:
                added_product = input("\nPlease enter the name of new product: ")
                added_product_price = float(
                    input("Please enter the price of the new product: "))

                products_list.append({
                    "name": added_product.capitalize(),
                    "price": added_product_price,

                })

                print(("\nThe following product '{}' has been added to the products list\n").format(
                    added_product))
                imf.writing_from_dict(products_csv_path, products_list)
                cont = input("Want to add another? (Y/N): \n")
                if cont.capitalize() == "N":
                    break


def creating_new_courier():
     while True:
                added_courier = input("\nPlease enter the name of new courier: ")
                added_courier_num = input(
                    "Please enter the number of the new courier: ")

                couriers_list.append({
                    "name": added_courier.capitalize(),
                    "phone": added_courier_num,

                })

                print(("\nThe following courier '{}' has been added to the couriers list\n").format(
                    added_courier))
                cont = input("Want to add another? (Y/N): \n")
                if cont.capitalize() == "N":
                    break


def updating_product():
    printing_dict(products_list, "Products")
    while True:
        try:
            product_update_index = int(input("\nSelect a product to update or 0 to cancel: \n"))
            products_list[product_update_index -1]
        except:
            print("\nInavalid Input\n")
            continue
        if product_update_index == 0:
            print("\nCancelled")
            print_divider()
            product_menu()
            break 
                        
        
        chosen_dict = (products_list[product_update_index - 1])
        update_product = input(
            "\nPlease enter updated name of product or leave blank to skip:\n")
        if update_product == "":
            left_blank()
        else:
            chosen_dict["name"] = update_product.capitalize()           
        
        #If i have my value as a float when i try to leave blank it throws error
        update_price = input(
            "\nPlease enter updated price for this product or leave blank to skip:\n")         
        
        # if update_price != float:
        #     print("Incorrect Value, enter a float")
        #     continue
        if update_price == "":
            left_blank()
        else:
            chosen_dict["price"] = update_price
            print_divider()   
        print("\nThe product has been updated successfully")
        imf.writing_from_dict(products_csv_path, products_list)
        cont = input("\nWant to update another? (Y/N): \n")
        if cont.capitalize() == "N":
            break


def updating_courier():
    printing_dict(couriers_list, "Couriers")
    while True:
        try:
            courier_update_index = int(input("\nSelect a product to update or 0 to cancel: \n"))
            couriers_list[courier_update_index -1]
        except:
            print("\nInavalid Input\n")
            continue
        if courier_update_index == 0:
            print("\nCancelled")
            print_divider()
            couriers_menu()
            break 

        chosen_dict = (couriers_list[courier_update_index - 1])
        update_courier_name = input("\nPlease enter updated name of courier or leave blank to skip:\n")

        if update_courier_name == "":
            left_blank()
        else:
            chosen_dict["name"] = update_courier_name.capitalize()
            update_courier_numb = input("\nPlease enter updated number for this courier or leave blank to skip:\n")
        if update_courier_numb == "":
            left_blank()
        else:
            chosen_dict["phone"] = update_courier_numb
            left_blank()

        print("The courier has been updated successfully\n")
        imf.writing_from_dict(couriers_csv_path, couriers_list)
        cont = input("\nWant to update another? (Y/N): \n")
        if cont.capitalize() == "N":
            break


def removing_dict(list_to_remove_dict, return_menu, subj):
    while True:
        try:
            print(("\nSelect a {} to remove or 0 to cancel").format(subj))
            remove_index = int(input(": "))
            list_to_remove_dict[remove_index -1]
        except:
            print("\nInavalid Input\n")
            continue
        if remove_index == 0:
            print("\nCancelled")
            print_divider()
            return_menu
            break 
        chosen_dict = (list_to_remove_dict[remove_index - 1])
        list_to_remove_dict.remove(chosen_dict)
        print_divider()
        print(("\nThe {} has been removed successfully").format(subj))
        cont = input("\nWant to remove another? (Y/N): \n")
        if cont.capitalize() == "N":
            break


def adding_product_index(): 
    order_products.clear()
    while True:
        try:
            value_input = int(input(": "))
            print(products_list)
            products_list[value_input -1]
        except:
            print("Incorrect command")
            continue
        if value_input == 0:
            print("\nYou have stopped adding products")
            break                 
        order_products.append(value_input)     
    print(("Products chosen {}") .format(order_products))


def choosing_courier_for_order():
    print("\nEnter the number that matches the courier you would like to choose \n")
    printing_dict(couriers_list, "Couriers")
    try:

    
        courier_index = int(input("\nCourier: "))
        while courier_index < 1 or courier_index > len(couriers_list):
            courier_index = int(input("\nPlease enter a valid number\n"))
        else:
            pass

    except ValueError:
        print("\nInavalid Input\n")
        choosing_courier_for_order()

    return courier_index    
        

def adding_new_order():
    while True:
                name = input("Give the name of the customer you want to add: ")
                address = input("\nAddress of customer: ")
                phone = int(input("\nEnter the phone number: "))

                print("\nPlease select from the numbered list below the products you would like to add. [0] to cancel ")

                printing_dict(products_list, "Products")

                adding_product_index()

                courier_index = choosing_courier_for_order()

                orders_list.append({
                        "customer_name": name.capitalize(),
                        "customer_address": address,
                        "customer_phone": phone,
                        "courier": courier_index,
                        "status": "Preparing",
                        "items": order_products 

                    })
                print("\nThe order has successfully been added\n")
                cont = input("Want to add another? (Y/N): \n")
                if cont.capitalize() == "N":
                    break


def choosing_order_status():
    order_status_options = ["Preparing", "Ready", "En route", "Delivered"]
    
    for index, status in enumerate(order_status_options, start=1):
        print(("{} | {}").format(index, status))
    
    new_status = int(input("\nSelect a new status from the options above: \n"))
    print("")
    while new_status < 1 or new_status > len(order_status_options):
        new_status = int(input("\nPlease enter a valid number\n"))
    else:
        pass

    if new_status == 1:
        chosen_status = order_status_options[0]
    elif new_status ==2:
        chosen_status = order_status_options[1]
    elif new_status ==3:
        chosen_status = order_status_options[2]
    elif new_status ==4:
        chosen_status = order_status_options[3]
    
    return chosen_status


def updating_order_status():        
    while True:
        try:
            order_index = int(input("\nSelect a order to update the status or 0 to cancel: \n"))
            orders_list[order_index -1]
        except:
            print("Incorrect command")
            continue
        if order_index == 0:
            print("\nCancelled")
            print_divider()
            order_menu()
            break 
        
        else:
            chosen_dict = (orders_list[order_index - 1])
            updated_status = choosing_order_status()

            chosen_dict['status'] = updated_status
            print_divider()
            print("The status of the order has now changed ")
            cont = input("Want to update another? (Y/N): \n")
            if cont.capitalize() == "N":
                break



def updating_order():
    while True:
        try:
            order_index = int(input("\nSelect a order to update or 0 to cancel: \n"))
            orders_list[order_index -1]
        except:
            print("Incorrect command")
            continue
        if order_index == 0:
            print("\nCancelled")
            print_divider()
            order_menu()
            break 
        
        else:
            chosen_dict = (orders_list[order_index - 1])
            
            new_name = input(
                    "\nPlease enter updated name or leave blank to skip:\n")
            if new_name == "":
                left_blank()
            else:
                chosen_dict["customer_name"] = new_name.capitalize()
                left_blank()

            new_address = input(
                "\nPlease enter updated address or leave blank to skip:\n")
            if new_address == "":
                left_blank()
            else:
                chosen_dict["customer_address"] = new_address.capitalize()
                print_divider()

            new_phone = input(
                "\nPlease enter updated number or leave blank to skip:\n")
            if new_phone == "":
                left_blank()
            else:
                chosen_dict["customer_phone"] = new_phone
                print_divider()
            

            print("\nPlease enter updated courier or leave blank to skip\n")
            printing_dict(couriers_list, "Couriers")

            new_courier = input("\nCourier:\n")
            if new_courier == "":
               print("\nSkipped")
            else:
               chosen_dict["courier"] = new_courier
               print_divider()

            updated_status = choosing_order_status()

            chosen_dict['status'] = updated_status
            print_divider()

        print("\nThe order has been updated successfully\n")
        cont = input("\nWant to update another? (Y/N): \n")
        if cont.capitalize() == "N":
            break


def printing_dict(chosen_menu_list, menu):
    for i, c_dict in enumerate(chosen_menu_list, start=1):
        print("")
        print(((color.BOLD + color.UNDERLINE + color.RED +
                "{} {}" + color.END)).format(menu, i))
        for key, value in c_dict.items():
            print(("{}: {}").format(key,value))



def main_menu():
    while True:

        print_divider()
        print("                           Welcome to 'MUNCH' cafe  ")
        print("\n")
        print("Please choose from the list below: \n \
        0. QUIT: \n \
        1. PRODUCT MENU: \n \
        2. COURIER MENU: \n \
        3. ORDER MENU: \n \
        ")

        
        select = int(input("Select your choice '0, 1, 2, 3':\n "))
        clear()
        print_divider()

        if select == 0:
            clear()
            print("Thank you for using the APP!\nSee you next time. Bye.")
            print(now.strftime("%I:%M:%S %p"))
            exit()

        if select == 1:
            product_menu()
            break

        if select == 2:
            couriers_menu()
            break

        if select == 3:
            order_menu()
            break

        else:
            clear()
            print("Invalid Input")
            continue


def product_menu():
    while True:
        
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
        clear()
        print_divider()

        if product_selected == 0:
            clear()
            print("\nYou have been redirected to the main menu")
            main_menu()
            break
    
        if product_selected == 1:
            clear()
            print("PRODUCTS...\n")
            printing_dict(products_list, "Products")
            break
    
        if product_selected == 2:
            clear()
            print("ADDING NEW PRODUCT...\n")
            creating_new_product()
            break
    
        if product_selected == 3:
            clear()
            print("UPDATING PRODUCT...\n")
            updating_product()
            break
    
        if product_selected == 4:
            clear()
            print("REMOVING PRODUCT...\n")
            printing_dict(products_list, "Products")
            removing_dict(products_list, product_menu, "product")
            break
        
        else:
            clear()
            print("Invalid Input")
            continue
    
    imf.writing_from_dict(products_csv_path, products_list)
    print("\nYou have been redirected to the product menu")
    print_divider()
    product_menu()


def couriers_menu():
    while True:
    
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
        clear()
        print_divider()

        if couriers_selected == 0:
            clear()
            print("\nYou have been redirected to the main menu")
            main_menu()
            break

        if couriers_selected == 1:
            clear()
            print("COURIERS...\n")
            printing_dict(couriers_list, "Couriers")
            break

        if couriers_selected == 2:
            clear()
            print("ADDING NEW COURIER...\n")
            creating_new_courier()
            break

        if couriers_selected == 3:
            clear()
            print("UPDATING COURIER...\n")
            updating_courier()
            break

        if couriers_selected == 4:
            clear()
            print("REMOVING COURIER...\n")
            printing_dict(couriers_list, "Couriers")
            removing_dict(couriers_list, couriers_menu, "courier")
            break

        else:
            clear()
            print("Invalid Input")
            continue

    imf.writing_from_dict(couriers_csv_path, couriers_list)
    print("\nYou have been redirected to the couriers menu ")
    print_divider()
    couriers_menu()


def order_menu():
    while True:

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
        clear()
        print_divider()

        if order_selected == 0:
            clear()
            print("\nYou have been redirected to the main menu")
            main_menu()
            break

        elif order_selected == 1:
            clear()
            print('Printing ORDERS...\n')
            # for i in orders_list:
                # print(i)
            printing_dict(orders_list, "Orders")
            break

        elif order_selected == 2:
            clear()
            print("ADDING NEW ORDER...\n")
            adding_new_order()
            break
        
        elif order_selected == 3:
            clear()
            print("UPDATING ORDER STATUS...\n")
            # for i in orders_list:
                # print(i)
            printing_dict(orders_list, "Orders")
            updating_order_status()
            break

        if order_selected == 4:
            clear()
            print("UPDATING ORDER...\n")
            printing_dict(orders_list, "Orders")
            updating_order()
            break

        if order_selected == 5:
            clear()
            print("REMOVING ORDER...\n")
            printing_dict(orders_list, "Orders")
            removing_dict(orders_list, order_menu, "order")
            break

        else:
            clear()
            print("Invalid Input")
            continue

    imf.writing_from_dict(orders_csv_path, orders_list)
    print("\nYou have been redirected to the orders menu ")
    print_divider()
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
    name = get_name().capitalize()
    clear()
    print_divider()

    create_greeting(name)

    imf.reading_from_dict(orders_csv_path, orders_list)
    imf.reading_from_dict(products_csv_path, products_list)
    imf.reading_from_dict(couriers_csv_path, couriers_list)


greetings()
main_menu()
