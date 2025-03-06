import csv

customer_data = [
    ['CustomerID', 'Name', 'Email'],
    [1, 'Fezco', 'Fezco@example.com'],
    [2, 'Jane Smith', 'jane.smith@example.com'],
    [3, 'Bob Johnson', 'bob.johnson@example.com'],
    [4, 'Alice Brown', 'alice.brown@example.com'],
    [5, 'Charlie Green', 'charlie.green@example.com'],
    [6, 'David White', 'david.white@example.com'],
    [7, 'Eve Black', 'eve.black@example.com'],
    [8, 'Frank Gray', 'frank.gray@example.com'],
    [9, 'Grace Blue', 'grace.blue@example.com'],
    [10, 'Henry Yellow', 'henry.yellow@example.com']
]

with open('customer.csv', mode='w', newline='') as customer_file:
    customer_writer = csv.writer(customer_file)
    customer_writer.writerows(customer_data)

orders_data = [
    ['OrderID', 'CustomerID', 'Product', 'Quantity', 'Price', 'OrderDate'],
    [1, 1, 'Product A', 5, 100, '2024-09-15'],
    [2, 2, 'Product B', 3, 200, '2024-10-20'],
    [3, 3, 'Product C', 2, 300, '2024-11-25'],
    [4, 4, 'Product D', 4, 400, '2025-01-05'],
    [5, 5, 'Product E', 1, 500, '2025-02-10'],
    [6, 6, 'Product F', 6, 600, '2025-03-15'],
    [7, 7, 'Product G', 3, 700, '2025-04-20'],
    [8, 8, 'Product H', 2, 800, '2025-05-25'],
    [9, 9, 'Product I', 4, 900, '2025-06-05'],
    [10, 10, 'Product J', 5, 1000, '2025-07-10']
]

with open('orders.csv', mode='w', newline='') as orders_file:
    orders_writer = csv.writer(orders_file)
    orders_writer.writerows(orders_data)

my_name = 'Fezco'
print(f"My name is: {my_name}")

import pandas as pd
import sqlite3

customers_df = pd.read_csv('customer.csv')
orders_df = pd.read_csv('orders.csv')

merged_df = pd.merge(orders_df, customers_df, on='CustomerID', how='inner')

merged_df['TotalSales'] = merged_df['Quantity'] * merged_df['Price']

merged_df['Status'] = merged_df['OrderDate'].apply(lambda d: 'New' if d > '2024-10-31' else 'Old')

high_value_orders = merged_df[merged_df['TotalSales'] > 500]

conn = sqlite3.connect('ecommerce.db')

create_table_query = '''
CREATE TABLE IF NOT EXISTS HighValueOrders (
    OrderID INTEGER,
    CustomerID INTEGER,
    Name TEXT,
    Email TEXT,
    Product TEXT,
    Quantity INTEGER,
    Price REAL,
    OrderDate TEXT,
    TotalSales REAL,
    Status TEXT
)
'''
conn.execute(create_table_query)

high_value_orders.to_sql('HighValueOrders', conn, if_exists='replace', index=False)

result = conn.execute('SELECT * FROM HighValueOrders')
for row in result.fetchall():
    print(row)

conn.close()

print("ETL process completed successfully!")