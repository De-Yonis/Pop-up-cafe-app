from datetime import datetime
# from file_handlers import txt as mf
from src.file_handlers import csv as imf
import os
import csv
import pymysql
from dotenv import load_dotenv
# import pandas as pd

# #Using Pandas 
# df = pd.read_csv('/Users/demo/Desktop/mini-project-folder/data/orders.csv')
# # rearrange column here for orders csv
# df_reorder = df[['status', 'customer_name', 'customer_address', 'customer_phone', 'courier', 'items']]  
# df_reorder.to_csv("/Users/demo/Desktop/VS Programming /My_projects/Mini_project/data /csv_files/orders.csv", index=False)

orders_csv_path = "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/data /csv_files/orders.csv"
couriers_csv_path = "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/data /csv_files/couriers.csv"
products_csv_path =  "/Users/demo/Desktop/VS Programming /My_projects/Mini_project/data /csv_files/products.csv"

#################################### Loading environment variables from .env file #################################### 
def establish_connection():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establishing a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
        )

#################################### #################################### #################################### 
products_list = []

products_cached = []
couriers_cached = []
orders_cached = []

product_id_list = []
courier_id_list = []
order_id_list = []

added_products = []

#################################### PRINTING FROM CACHED LISTS P,C,O ####################################
def print_products_cached():
    for row in products_cached:
        print(f"Product ID {str(row[0])} - Name: {row[1]}, Price: £{row[2]}")

def print_couriers_cached():
    for row in couriers_cached:
         print(f'Courier ID {str(row[0])} - Name: {row[1]}, Number: 0{row[2]}')

def print_orders_cached():
    for row in orders_cached:
        print(f'Order ID {str(row[0])} - Status: {row[1]}, Customer Name: {row[2]}, Address: {row[3]}, Phone Number: 0{str(row[4])}, Courier: {row[5]}, Items: {row[6]}')

##################################### P,C & O - ID's for ERROR HANDLING ####################################

def get_ids_from_db(table, id_list):
    with connection.cursor() as cursor:
    
        if table == "couriers":
            sql = "SELECT courier_id FROM couriers"
            cursor.execute(sql)
            my_result = cursor.fetchall()
            id_list.clear()
            for id in my_result:
                id_list.append(id[0])
           

        elif table == "products":
            sql = "SELECT product_id FROM products"
            cursor.execute(sql)
            my_result = cursor.fetchall()
            id_list.clear()
            for id in my_result:
                id_list.append(id[0])

        elif table == "orders":
            sql = "SELECT order_id FROM orders"
            cursor.execute(sql)
            my_result = cursor.fetchall()
            id_list.clear()
            for id in my_result:
                id_list.append(id[0])

##################################### P,C & O - CACHE DATABASE TO LISTS ####################################

def refresh_cached_products():
    products_cached.clear()
    with connection.cursor() as cursor:
        # Execute SQL query
        cursor.execute('SELECT * FROM products')
        # Gets all rows from the result
        rows = cursor.fetchall()
        for row in rows:
            products_cached.append(row)

def refresh_cached_couriers():
    couriers_cached.clear()
    with connection.cursor() as cursor:
        # Execute SQL query
        cursor.execute('SELECT * FROM couriers')
        # Gets all rows from the result
        rows = cursor.fetchall()
        for row in rows: 
            couriers_cached.append(row)

def refresh_cached_orders():
    orders_cached.clear()
    with connection.cursor() as cursor:
        # Execute SQL query
        cursor.execute('SELECT * FROM orders')
        # Gets all rows from the result
        rows = cursor.fetchall()
        for row in rows:
            orders_cached.append(row)

#################################### ADDING TO THE DATABASE P & C #################################### 

def add_to_db(menu,table,second_row):
    with connection.cursor() as cursor:
        
        sql = (("INSERT INTO {} (name, {}) VALUES (%s, %s)").format(table, second_row))

        val = (create_new_name(menu), create_second_row_value(menu,second_row))
        
        cursor.execute(sql, val)
        connection.commit()
        print("")
        clear()
        print(("You have have successfully added a new {}.\n").format(menu))
        
def create_new_name(menu):
    name_input = input("\nWhat is the name of the {}: ".format(menu))
    name = name_input.title()
    return name

def create_second_row_value(menu, second_row):
    while True:
        try:
            new_value = input("\nWhat is the {} of the {} you would like to add: ".format(second_row, menu))
            if second_row == 'price':
                price_value = float(new_value)
                return price_value
            
            elif second_row == 'phone':
                phone_cour = int(new_value)
                return phone_cour
                
        except ValueError:
            print("\nInvalid Input (please enter a number)\n")

#################################### UPDATING THE DATABASE P & C #################################### 

def id_chosen_for_updating(table, menu, id_list):
    get_ids_from_db(table, id_list)
    
    while True:
        try:
            id_input = int(input(("\nPlease enter the id of the {} you would like to update or [0] to cancel:\n").format(menu)))

            if id_input == 0:
                clear()
                main_menu()
                break

            elif id_input not in id_list:
                print("\nInvalid id chosen\n")
                continue
            
            else:
                index = id_input
                return index
                # break
        
        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
            continue

def update_name(menu, table):
    name_input = input("\nPlease enter the new name of the {} or leave blank to skip: ".format(menu))
    if name_input == "":
        clear()
        left_blank()
        pass
    else: 
        name = name_input.title()
        return name

def update_to_db_name(menu, table, id_list, needed_id):
    new_name = update_name(menu, table)
    if new_name == None:
        pass
    else:    
        with connection.cursor() as cursor:
            if table == "products":
                sql_command = "UPDATE products SET name = %s WHERE product_id = %s"
            elif table == "couriers":
                sql_command = "UPDATE couriers SET name = %s WHERE courier_id = %s " 
            value = (new_name,needed_id)
            cursor.execute(sql_command, value)
            connection.commit()
            print("")
            clear()
            print(("The chosen {} name has successfully been updated.\n").format(menu))
    return needed_id

def update_second_row_value(menu, second_row):
    while True:
        try:
            new_value = input("\nPlease enter the {} of the new {} or leave blank to skip:\n".format(second_row, menu))
            if new_value == "":
                clear()
                left_blank()
                break
            if second_row == 'price':
                price_value = float(new_value)
                return price_value
                # break
            elif second_row == 'phone':
                phone_cour = int(new_value)
                return phone_cour
                # break
                
        except ValueError:
            print("\nInvalid Input (please enter a number)\n")

def update_to_db_attribute(menu, table, second_row, needed_id):
    needed_value = update_second_row_value(menu, second_row)
    
    if needed_value == None:
        pass
    else:
        with connection.cursor() as cursor:

            if table == "products":
                    sql_command = "UPDATE products SET price = %s WHERE product_id = %s "

            elif table == "couriers":
                    sql_command = "UPDATE couriers SET phone = %s WHERE courier_id = %s "

            value = (needed_value,needed_id)
            cursor.execute(sql_command, value)
            connection.commit()
            print("")
            clear()
            print(("The chosen {} {} has successfully been updated.\n").format(menu, second_row))
            # print(cursor.rowcount, "updated.")

#################################### REMOVING FROM THE DATABASE P,C & O #################################### 

def removing_db(table, menu, id_list):
    with connection.cursor() as cursor:

        if table == "products":
            sql_command = "DELETE FROM products WHERE product_id = %s"

        elif table == "couriers":
            sql_command = "DELETE FROM couriers WHERE courier_id = %s"
        
        elif table == "orders":
            sql_command = "DELETE FROM orders WHERE order_id = %s"

        value = (id_chosen_for_removing(table, menu, id_list))
        cursor.execute(sql_command, value)
        connection.commit() 
        print("")
        clear()
        print(("The chosen {} has successfully been removed.\n").format(menu))
        # print(cursor.rowcount, "removed.")
    
def id_chosen_for_removing(table, menu, id_list):
    get_ids_from_db(table, id_list)
    while True:
        try:
            id_input = int(input(("\nPlease enter the id of the {} you would like to remove or [0] to cancel:\n").format(menu)))

            if id_input == 0:
                clear()
                main_menu()
                break

            elif id_input not in id_list:
                print("\nInvalid id chosen\n")
                continue
            
            else:
                index = id_input
                return index
                # break
        
        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
            continue

#################################### ADDING TO THE ORDER TABLE ####################################

def get_customer_name():
    clear()
    added_customer = input("\nPlease enter the name of customer: ")
    return added_customer.title()

def get_customer_address():
    clear()
    added_address = input("\nPlease enter the address of customer you would like to add: ")
    return added_address.title()

def get_customer_number():
    clear()
    while True:
        try:
            phone_numb = int(input("\nPlease enter the phone number: "))
            return phone_numb
            # break
        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
        except EOFError:
            print("Please input a value")

def get_courier():
    clear()
    while True:
        get_ids_from_db('couriers', courier_id_list)
        print("")
        print_couriers_cached()
        try: 
            print("\nPlease select a courier from the list above")
            courier_input = int(input("courier_id: "))
            
            if courier_input not in courier_id_list:
                clear()
                print("\nInvalid Input (please enter an id from the options provided)\n")

            else:
                courier_chosen = courier_input
                return courier_chosen
                # break

        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
                
def get_default_status():
    clear()
    default_status = "Preparing"
    return default_status

def get_order_products():
    clear()
    get_ids_from_db("products",product_id_list)
    print("")
    added_products.clear()
    print_products_cached()
    print("\nPlease choose from the list above the ids of the products you would like to add, [0] to stop adding ")
    
    while True:
        try:
            chosen_products = int(input("Product: "))
            
            if chosen_products == 0:
                print("\nYou have stopped adding products")
                break
            
            elif chosen_products not in product_id_list:
                print("\nInvalid Input (please enter a id from the options provided)\n")
                continue
            
            added_products.append(chosen_products)
            # print(added_products)

        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
            continue

            
    print(("Products chosen {}").format(added_products))
    return str(added_products)

def adding_new_order_db():
    with connection.cursor() as cursor:
        
        sql = (("INSERT INTO orders (status,customer_name,customer_address,customer_phone,courier_id,items) VALUES (%s,%s,%s,%s,%s,%s)"))

        val = (get_default_status(), get_customer_name(), get_customer_address(), get_customer_number(), get_courier(), get_order_products())
        
        cursor.execute(sql, val)
        connection.commit()
        print("")
        clear()
        print(("You have successfully added a new order.\n"))
        # print(cursor.rowcount, "added.")

#################################### UPDATING ORDER STATUS ####################################

def id_chosen_for_order_status():
    get_ids_from_db('orders', order_id_list)
    print_orders_cached()
    while True:
        try:
            id_input = int(input(("\nPlease enter the id of the order you would like to update the status or [0] to cancel:\n")))

            if id_input == 0:
                clear()
                order_menu()
                

            elif id_input not in order_id_list:
                print("\nInvalid id chosen\n")
                continue
            
            else:
                index = id_input
                return index
                
        
        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
            continue

def get_order_status():
    clear()
    while True:
        try:
            print(f"{color.RED}{color.BOLD}                ORDER STATUS OPTIONS{color.END}")
            order_status_options = ["Preparing", "Ready", "En route", "Delivered"]

            for index, status in enumerate(order_status_options, start=1):
                print(("{} | {}").format(index, status))

            new_status = int(input("\nPlease select a new status from the options above: \n"))
            print("")
            
            if new_status < 1 or new_status > len(order_status_options):
                clear()
                print("\nPlease enter a valid number\n")
                continue

            else:
                break
            
        except ValueError:
            clear()
            print("\nInavalid Input\n")
       
    if new_status == 1:
        chosen_status = order_status_options[0]
    elif new_status == 2:
        chosen_status = order_status_options[1]
    elif new_status == 3:
        chosen_status = order_status_options[2]
    elif new_status == 4:
        chosen_status = order_status_options[3]

    return chosen_status
    
def update_order_status():
    chosen_id = id_chosen_for_order_status()

    with connection.cursor() as cursor:
    
        sql_command = "UPDATE orders SET status = %s WHERE order_id = %s"
   
        value = (get_order_status(),chosen_id)
        cursor.execute(sql_command, value)
        connection.commit()
        print("")
        clear()
        print(("The order status has successfully been updated.\n"))
        # print(cursor.rowcount, "updated.")

################################### UPDATING ORDER IN DATABASE ####################################
def get_id_for_updating_order():
    get_ids_from_db('orders', order_id_list)
    print_orders_cached()
    while True:
        try:
            id_input = int(input(("\nPlease enter the id of the order you would like to update or [0] to cancel:\n")))

            if id_input == 0:
                clear()
                order_menu()
                break

            elif id_input not in order_id_list:
                print("\nInvalid id chosen\n")
                continue
            
            else:
                index = id_input
                return index
                # break
        
        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
            continue

def update_customer_name():
    name_input = input("\nPlease enter the new name of the customer or leave blank to skip: ")
    if name_input == "":
        clear()
        left_blank()
        pass
    else: 
        name = name_input.title()
        return name

def update_customer_name_db(update_order_id):
    new_name = update_customer_name()
    if new_name == None:
        pass
    else:    
        with connection.cursor() as cursor:

            sql_command = "UPDATE orders SET customer_name = %s WHERE order_id = %s " 
            
            value = (new_name,update_order_id)

            cursor.execute(sql_command, value)
            connection.commit()
            print("")
            clear()
            print("The customer name has successfully been updated\n")
            # print(cursor.rowcount, "updated.")
    return update_order_id

def update_customer_address():
    address_input = input("\nPlease enter the new address of the order or leave blank to skip: ")
    if address_input == "":
        clear()
        left_blank()
        pass
    else: 
        address = address_input.title()
        return address

def update_customer_address_db(update_order_id):
    new_address = update_customer_address()
    if new_address == None:
        pass
    else:    
        with connection.cursor() as cursor:

            sql_command = "UPDATE orders SET customer_address = %s WHERE order_id = %s " 
            
            value = (new_address,update_order_id)

            cursor.execute(sql_command, value)
            connection.commit()
            print("")
            clear()
            print("The address has successfully been updated\n")
            # print(cursor.rowcount, "updated.")
    return update_order_id

def update_customer_phone():
     while True:
        try:
            number_input = input("\nPlease enter the phone number or leave blank to skip:\n")
            if number_input == "":
                clear()
                left_blank()
                break
            else:
                number = float(number_input)
                return number
                # break

        except ValueError:
            print("\nInvalid Input (please enter a number)\n")

def update_customer_phone_db(update_order_id):
    new_number = update_customer_phone()
    if new_number == None:
        pass
    else:    
        with connection.cursor() as cursor:

            sql_command = "UPDATE orders SET customer_phone = %s WHERE order_id = %s " 
            
            value = (new_number, update_order_id)

            cursor.execute(sql_command, value)
            connection.commit()
            print("")
            clear()
            # print(cursor.rowcount, "updated.")
            print("The number has successfully been updated\n")
    return update_order_id

def update_courier():
    while True:
        get_ids_from_db('couriers', courier_id_list)
        print("")
        print_couriers_cached()
        try: 
            print("\nPlease select a new courier from the list above or leave blank to skip")
            courier_input = input(("courier_id: "))

            if courier_input == "":
                clear()
                left_blank()
                break
            
            else:
                courier_input = int(courier_input)
                
                if courier_input not in courier_id_list:
                    print("\nInvalid Input (please enter an id from the options provided)\n")
                    continue

                elif courier_input in courier_id_list:
                    courier_chosen = int(courier_input)
                    return courier_chosen
                    # break

        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
            continue

def update_courier_db(update_order_id):
    new_courier = update_courier()
    if new_courier == None:
        pass
    else:    
        with connection.cursor() as cursor:

            sql_command = "UPDATE orders SET courier_id = %s WHERE order_id = %s " 
            
            value = (new_courier, update_order_id)

            cursor.execute(sql_command, value)
            connection.commit()
            print("")
            clear()
            # print(cursor.rowcount, "updated.")
            print("The courier has successfully been updated\n")
    return update_order_id

def update_order_products_prompt():
    print("\nEnter [1] to update the order products or leave blank to skip:")
    
    chosen_option = input()

    if chosen_option == "1":
        print("\nUpdating Products in Order\n")
        updated_products = update_added_order_products()
        return updated_products

    elif chosen_option == "":
        clear()
        left_blank()
        pass

    else:
        update_order_products_prompt()

def update_added_order_products():
    get_ids_from_db("products",product_id_list)
    added_products.clear()
    print_products_cached()
    print("\nPlease choose from the list above the id's of the products you would like to add, [0] to stop adding ")
    
    while True:
        try:
            chosen_products = int(input("Product: "))
            
            if chosen_products == 0:
                print("\nYou have stopped adding products")
                break
            
            elif chosen_products not in product_id_list:
                print("\nInvalid Input (please enter a id from the options provided)\n")
                continue
            
            added_products.append(chosen_products)
            # print(added_products)

        except ValueError:
            print("\nInvalid Input (please enter a number)\n")
            continue

            
    print(("Products chosen {}").format(added_products))
    return str(added_products)
    
def update_added_order_products_db(update_order_id):
    new_added_products = update_order_products_prompt()
    if new_added_products == None:
        pass
    else:    
        with connection.cursor() as cursor:

            sql_command = "UPDATE orders SET items = %s WHERE order_id = %s " 
            
            value = (new_added_products, update_order_id)

            cursor.execute(sql_command, value)
            connection.commit()
            print("")
            clear()
            print("The product items has successfully been updated\n")
            # print(cursor.rowcount, "updated.")
   
#################################### #################################### #################################### 

now = datetime.now()

def clear(): return os.system('cls' if os.name == 'nt' else 'clear')

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

def left_blank():
    print(f"{color.YELLOW}\nYou have skipped this option{color.END}")

def print_divider():
    print(80 * f"{color.BOLD}-{color.END}")
#################################### FUNCTIONS FOR PRODUCT MENU ADDS TO CSV #################################### 

def printing_product_dict():
    for i, c_dict in enumerate(products_list, start=1):
        print("")
        print(((color.BOLD + color.UNDERLINE + color.RED +
                "Product {}" + color.END)).format(i))
        for key, value in c_dict.items():
            print(("{}: {}").format(key, value))

def get_new_product_name():
    added_product = input("\nPlease enter the name of new product: ")
    return added_product.title()

def get_new_product_price():
    added_product_price = float(input("Please enter the price of the new product: "))
    return added_product_price

def create_new_product(name, price):
    return {"name": name, "price": price}

def add_product_to_cache(product, inventory=products_list):
    inventory.append(product)
    return inventory

def creating_new_product():
    name = get_new_product_name()
    price = get_new_product_price()
    new_product = create_new_product(name, price)

    try:
        add_product_to_cache(new_product)
        print(("\nThe following product '{}' has been added to the products list\n").format(
            new_product
        ))
    except Exception as e:
        print(e)

################################################ RUNNING MENUS #############################################

def main_menu():
    while True:

        print_divider()
        print(f"{color.RED}{color.BOLD}                           Welcome to 'MUNCH' cafe  {color.END}")
        print("\n")
        print("Please choose from the list below: \n \
        0. QUIT: \n \
        1. PRODUCT MENU: \n \
        2. COURIER MENU: \n \
        3. ORDER MENU: \n \
        ")
        
        select = int(input("Select your choice '0, 1, 2, 3':\n"))
        clear()
        print_divider()

        if select == 0:
            clear()
            log_out()

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
        print(f"{color.RED}{color.BOLD}                                   PRODUCTS{color.END} ")
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
            print(f"{color.RED}{color.BOLD}\nYou have been redirected to the main menu{color.END}")
            main_menu()
            break

        if product_selected == 1:
            clear()
            print(f"{color.RED}{color.BOLD}PRODUCTS...\n{color.END}")
            # printing_product_dict()
            print_products_cached()
            print
            break

        if product_selected == 2:
            clear()
            print(f"{color.RED}{color.BOLD}ADDING NEW PRODUCT...\n{color.END}")
            # creating_new_product()
            add_to_db('product', 'products', 'price')
            break

        if product_selected == 3:
            clear()
            print(f"{color.RED}{color.BOLD}UPDATING PRODUCT...\n{color.END}")
            print_products_cached()
            needed_id = id_chosen_for_updating('products','product',product_id_list) 
            # print("Needed id is at this point", needed_id)
            update_to_db_name('product', 'products', product_id_list, needed_id)
            update_to_db_attribute('product', 'products', 'price', needed_id)
            break

        if product_selected == 4:
            clear()
            print(f"{color.RED}{color.BOLD}REMOVING PRODUCT...\n{color.END}")
            print_products_cached()
            removing_db('products', 'product', product_id_list)
            break

        else:
            clear()
            print(f"{color.RED}{color.BOLD}Invalid Input{color.END}")
            continue

    mf.writing_from_dict(products_csv_path, products_list)    
    refresh_cached_products()
    print(f"{color.RED}{color.BOLD}\nYou have been redirected to the product menu{color.END}")
    print_divider()
    product_menu()

def couriers_menu():
    while True:

        print("")
        print(f"{color.RED}{color.BOLD}                                COURIERS {color.END}")
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
            print(f"{color.RED}{color.BOLD}\nYou have been redirected to the main menu{color.END}")
            main_menu()
            break

        if couriers_selected == 1:
            clear()
            print(f"{color.RED}{color.BOLD}COURIERS...\n{color.END}")
            print_couriers_cached()
            break

        if couriers_selected == 2:
            clear()
            print(f"{color.RED}{color.BOLD}ADDING NEW COURIER...\n{color.END}")
            add_to_db('courier', 'couriers', 'phone')
            break

        if couriers_selected == 3:
            clear()
            print(f"{color.RED}{color.BOLD}UPDATING COURIER...\n{color.END}")
            
            print_couriers_cached()
            # print("Needed id is at this point is:", needed_id)
            needed_id = id_chosen_for_updating('couriers','courier',courier_id_list) 
            update_to_db_name('courier','couriers',courier_id_list, needed_id)
            update_to_db_attribute('courier','couriers', 'phone', needed_id)
            break

        if couriers_selected == 4:
            clear()
            print(f"{color.RED}{color.BOLD}REMOVING COURIER...\n{color.END}")
            print_couriers_cached()
            removing_db('couriers', 'courier', courier_id_list)
            break

        else:
            clear()
            print(f"{color.RED}{color.BOLD}Invalid Input{color.END}")
            continue
    
    refresh_cached_couriers()
    print(f"{color.RED}{color.BOLD}\nYou have been redirected to the couriers menu {color.END}")
    print_divider()
    couriers_menu()

def order_menu():
    while True:

        print("")
        print(f"{color.RED}{color.BOLD}                                    ORDERS {color.END}")
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
            print(f"{color.RED}{color.BOLD}\nYou have been redirected to the main menu{color.END}")
            main_menu()
            break

        elif order_selected == 1:
            clear()
            print(f"{color.RED}{color.BOLD}\nPrinting ORDERS...\n{color.END}")
            print_orders_cached()
            break

        elif order_selected == 2:
            clear()
            print(f"{color.RED}{color.BOLD}\nADDING NEW ORDER...\n{color.END}")
            adding_new_order_db()
            break

        elif order_selected == 3:
            clear()
            print(f"{color.RED}{color.BOLD}\nUPDATING ORDER STATUS...\n{color.END}")
            update_order_status()
            break

        if order_selected == 4:
            clear()
            print(f"{color.RED}{color.BOLD}\nUPDATING ORDER...\n{color.END}")
            update_order_id = get_id_for_updating_order()
            update_customer_name_db(update_order_id)
            update_customer_address_db(update_order_id)
            update_customer_phone_db(update_order_id)
            update_courier_db(update_order_id)
            update_added_order_products_db(update_order_id)
            break

        if order_selected == 5:
            clear()
            print(f"{color.RED}{color.BOLD}\nREMOVING ORDER...\n{color.END}")
            print_orders_cached()
            removing_db('orders', 'order', order_id_list)
            break

        else:
            clear()
            print(f"{color.RED}{color.BOLD}Invalid Input{color.END}")
            continue

    refresh_cached_orders()
    print(f"{color.RED}{color.BOLD}\nYou have been redirected to the orders menu{color.END} ")
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
    
    name = get_name().title()
    clear()
    print_divider()
    create_greeting(name)
    
    refresh_cached_products()
    refresh_cached_couriers()
    refresh_cached_orders()
    
    mf.reading_from_dict(products_csv_path, products_list)

def log_out():
    clear()
    print(now.strftime("%I:%M:%S %p"))
    connection.close()
    print(f"{color.BOLD}Thank you for using the APP!\nSee you next time. Bye.{color.END}")
    exit()

#################################### #################################### #################################### 
if __name__ == "__main__":
    establish_connection()
    greetings()
    main_menu()
