import csv

def writing_from_dict(file_name, file_info):
    try:
        csv_file = file_info
        with open(file_name, mode='w', encoding='utf8', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=csv_file[0].keys(),)
            writer.writeheader()
            writer.writerows(csv_file)
    except FileNotFoundError as fnf:
        print("Unable to open file: " + str(fnf))
    except Exception as e:
        print("The following error has occurred: " + str(e))


def reading_from_dict(file_name, file_info):
    try:
        with open(file_name, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                for key in row:
                    if key == "price":
                        row[key] = float(row[key])
                file_info.append(row)

    except FileNotFoundError as fnf:
        print("Unable to open file: " + str(fnf))
    except Exception as e:
        print("The following error has occurred: " + str(e))


# def writing_from_products_dict():
#     product_csv = products_list
#     with open('products.csv', mode='w', encoding='utf8', newline='') as output_file:
#         writer = csv.DictWriter(output_file, fieldnames=product_csv[0].keys(),)
#         writer.writeheader()
#         writer.writerows(product_csv)


# def reading_from_product_dict():
#     with open("products.csv", 'r') as file:
#         product_csv_file = csv.DictReader(file)
#         for row in product_csv_file:
#             products_list.append(row)


# def writing_from_couriers_dict():
#     courier_csv = couriers_list
#     with open('couriers.csv', mode='w', encoding='utf8', newline='') as output_file:
#         writer = csv.DictWriter(output_file, fieldnames=courier_csv[0].keys(),)
#         writer.writeheader()
#         writer.writerows(courier_csv)


# def reading_from_couriers_dict():
#     with open("couriers.csv", 'r') as file:
#         courier_csv_file = csv.DictReader(file)
#         for row in courier_csv_file:
#             couriers_list.append(row)


# def writing_from_order_dict():
#     order_csv = orders_list
#     with open('orders.csv', mode='w', encoding='utf8', newline='') as output_file:
#         writer = csv.DictWriter(output_file,
#                                 fieldnames=order_csv[0].keys(),

#                                 )
#         writer.writeheader()
#         writer.writerows(order_csv)


# def reading_from_order_dict():
#     with open("orders.csv", 'r') as file:
#         csv_file = csv.DictReader(file)
#         for row in csv_file:
#             orders_list.append(row)
