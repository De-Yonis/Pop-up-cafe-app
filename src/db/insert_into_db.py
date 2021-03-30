import pymysql
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
  
cursor = connection.cursor()




#Inserting Values staright from my CSV into database
with open('/Users/demo/Desktop/mini-project-folder/data/orders.csv', 'r') as csv_file:
    csv_reader =  csv.reader(csv_file)
    next (csv_reader)
    for row in csv_reader:
        status = row[0]
        customer_name = row[1]
        customer_address = row[2]
        customer_phone = row[3]
        courier = row[4]
        items = row [5]
        cursor.execute('INSERT INTO orders (status,customer_name,customer_address,customer_phone,courier_id,items) VALUES (%s,%s,%s,%s,%s,%s)', (status,customer_name,customer_address,customer_phone,courier,items))

connection.commit()




