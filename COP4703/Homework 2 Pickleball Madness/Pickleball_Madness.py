#
# Homework #2: Pickleball Madness
#
# 1.	You know that you've got to go back to school, so you want to 
# create a solution that your Aunt Mary can use long after you are gone. 
# You have decided that you are going to write a Python program that she 
# can use to get the answers that she needs about how her store is doing.
#
# 2.	Using Python and SQLite, you will create a Python program that 
# will create a database with the appropriate four tables that Aunt Mary 
# will need to store information about her store.
#
# 3.	You will then load these tables with the information that is 
# provided.
#
# 4.	You will then use your Python program to answer the following 
# questions:
# a.	What customers (first name, last name, address, city, state, zip 
# code) purchased Pickleball products?
#
# b.	Of the customers in Aunt Mary’s database, which ones have made a 
# purchase?
#
# c.	Of the products in Aunt Mary’s inventory, what products have been 
# sold?
#
# d.	How much money did Aunt Mary make selling Pickleball products?
#
# e.	How much money did Aunt Mary make selling Tennis products?
#
# f.	How much money did Aunt Mary make on her first sale?
# g.	How much money did Aunt Mary make on her last sale?
# h.	Create a result that shows each customer’s (first name, last name, 
# state) who has made a purchase.
#
# Student Name:
# Thurmond Guy

import sqlite3

conn = sqlite3.connect('Pickleball_Madness.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Customer
                (customer_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                zip_code TEXT,
                phone_number TEXT
                )''')

c.execute('''CREATE TABLE IF NOT EXISTS Product
                (product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                description TEXT,
                category TEXT,
                vendor_id INT,
                vendor_name TEXT
                )''')

c.execute('''CREATE TABLE IF NOT EXISTS Purchase
                (invoice_no INTEGER PRIMARY KEY,
                customer_id INTEGER,
                invoice_date TEXT,
                total_sale REAL,
                total_paid REAL,
                form_of_payment TEXT,
                FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
                )''')

c.execute('''CREATE TABLE IF NOT EXISTS Sold_Item
                (line_no INTEGER PRIMARY KEY,
                invoice_no INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (invoice_no) REFERENCES Purchase(invoice_no),
                FOREIGN KEY (product_id) REFERENCES Product(product_id)
                )''')

c.execute('''INSERT INTO Customer VALUES
                (1, 'Bob', 'Johnson', '1234 Main St', 'Tampa', 'FL', '33660', '813-555-1234'),
                (2, 'Ann', 'Majors', '675 Oak Ln', 'Oakland', 'CA', '12345', '425-555-2468'),
                (3, 'Barb', 'Sweeny', '34 Pine Rideg', 'Orlando', 'FL', '98765', '765-555-9476'),
                (4, 'Art', 'Puett', '123 Apple Way', 'Dallas', 'TX', '24680', '123-555-8765'),
                (5, 'Bobbi', 'Marschall', '98 Jenkins Dr', 'St. Louis', 'MO', '13579', '614-555-9123'),
                (6, 'Les', 'Peterson', '450 Pikes St', 'Tampa', 'FL', '98765', '845-555-7284'),
                (7, 'Amanda', 'Maples', '389 Lewis Rd', 'Miami', 'FL', '54321', '175-555-9274'),
                (8, 'Jenny', 'McPherson', '48 Alta Vista Dr', 'Los Angles', 'CA', '86420', '882-555-4423'),
                (9, 'Mike', 'Diesen', '12 Pointer Ln', 'New York', 'NY', '97531', '782-555-4444'),
                (10, 'Robert', 'Makely', '925 State St', 'Lakeland', 'FL', '16028', '345-555-6667')
                ''')

c.execute('''INSERT INTO Product VALUES
                (1, 'Pickleball Paddle', 'Paddle for Pickleball', 'Pickleball', 100, 'Pickle Prodcuts'),
                (2, 'Tennis Ball', 'Ball to use in Tennis', 'Tennis', 200, 'Tennis World'),
                (3, 'Ping Pong Paddle', 'Paddle for Ping Pong', 'Ping Pong', 300, 'Ping Pong Products'),
                (4, 'Squash Racket', 'Racket for Squash', 'Squash', 400, 'Squash Masters'),
                (5, 'Racquetball ball', 'Ball to use in Racquetball', 'Racquetball', 500, 'Racquetball Outlet'),
                (6, 'Badminton Racket', 'Racket for Badminton', 'Badmniton', 600, 'Badminton Universe'),
                (7, 'Pickleball Net', 'Net for Pickleball', 'Pickleball', 100, 'Pickle Prodcuts'),
                (8, 'Pickleball Ball', 'Ball to use in Pickleball', 'Pickleball', 100, 'Pickle Prodcuts'),
                (9, 'Tennis Racket', 'Racket for Tennis', 'Tennis', 200, 'Tennis World'),
                (10, 'Badminton Net', 'Net for Badminton', 'Badminton', 600, 'Badminton Universe')
                ''')

c.execute('''INSERT INTO Purchase VALUES
                (1, 2, '05/01/23', 125.86, 125.86, 'Cash'),
                (2, 2, '05/02/23', 75.25, 75.25, 'Check'),
                (3, 2, '05/03/23', 209.15, 209.15, 'Credit'),
                (4, 1, '05/04/23', 55.54, 55.54, 'Credit'),
                (5, 10, '05/05/23', 32.13, 32.13, 'Credit'),
                (6, 7, '05/06/23', 25.75, 25.75, 'Cash'),
                (7, 6, '05/07/23', 111.14, 111.14, 'Bitcoin'),
                (8, 5, '05/08/23', 89.72, 89.72, 'Credit'),
                (9, 3, '05/09/23', 12.24, 12.24, 'Cash'),
                (10, 8, '05/10/23', 62.34, 62.34, 'Cash')
                ''')

c.execute('''INSERT INTO Sold_Item VALUES
                (1, 1, 1, 10, 11.70),
                (2, 2, 10, 2, 34.99),
                (3, 3, 4, 1, 194.51),
                (4, 4, 2, 7, 7.38),
                (5, 5, 8, 5, 5.98),
                (6, 6, 6, 4, 5.99),
                (7, 7, 1, 2, 51.68),
                (8, 8, 9, 8, 10.43),
                (9, 9, 3, 3, 3.79),
                (10, 10, 1, 5, 11.60)
                ''')

c.execute('''SELECT Customer.first_name, Customer.last_name, Customer.address, Customer.city, Customer.state, Customer.zip_code
                FROM Customer
                JOIN Purchase ON Customer.customer_id = Purchase.customer_id
                JOIN Sold_Item ON Purchase.invoice_no = Sold_Item.invoice_no
                JOIN Product ON Sold_Item.product_id = Product.product_id
                WHERE Product.category = 'Pickleball'
                ''')

print('Customers who purchased Pickleball items:')
for row in c.fetchall():
    print(row)

c.execute('''SELECT DISTINCT Customer.first_name, Customer.last_name
                FROM Customer
                JOIN Purchase ON Customer.customer_id = Purchase.customer_id
                ''')

print('\nCustomers who have made a purchase:')
for row in c.fetchall():
    print(row)

c.execute('''SELECT Product.product_id, Product.product_name, Product.description, Product.category
                FROM Product
                JOIN Sold_Item ON Product.product_id = Sold_Item.product_id
                ''')

print('\nProducts that have been sold:')
for row in c.fetchall():
    print(row)

c.execute('''SELECT SUM(Sold_Item.quantity * Sold_Item.price)
                FROM Sold_Item
                JOIN Product ON Sold_Item.product_id = Product.product_id
                WHERE Product.category = 'Pickleball'
                ''')

print('\nMoney made from Pickleball products:')
for row in c.fetchall():
    total_money = (row[0])
    print(f"${total_money:.2f}")


c.execute('''SELECT SUM(Sold_Item.quantity * Sold_Item.price)
                FROM Sold_Item
                JOIN Product ON Sold_Item.product_id = Product.product_id
                WHERE Product.category = 'Tennis'
                ''')

print('\nMoney made from Tennis products:')
for row in c.fetchall():
    total_money = (row[0])
    print(f"${total_money:.2f}")

c.execute('''SELECT SUM(Sold_Item.quantity * Sold_Item.price)
                FROM Sold_Item
                JOIN Purchase ON Sold_Item.invoice_no = Purchase.invoice_no
                WHERE Purchase.invoice_no = 1
                ''')

print('\nMoney made from Aunt Mary\'s first sale:')
for row in c.fetchall():
    total_money = (row[0])
    print(f"${total_money:.2f}")

c.execute('''SELECT SUM(Sold_Item.quantity * Sold_Item.price)
                FROM Sold_Item
                JOIN Purchase ON Sold_Item.invoice_no = Purchase.invoice_no
                WHERE Purchase.invoice_no = 10
                ''')

print('\nMoney made from Aunt Mary\'s last sale:')
for row in c.fetchall():
    total_money = (row[0])
    print(f"${total_money:.2f}")


c.execute('''SELECT DISTINCT Customer.first_name, Customer.last_name, Customer.state
                FROM Customer
                JOIN Purchase ON Customer.customer_id = Purchase.customer_id
                ''')

print('\nCustomers who have made a purchase:')
for row in c.fetchall():
    print(row)


conn.commit()

conn.close()

