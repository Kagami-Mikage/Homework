import sqlite3

# Create a connection to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create Users table
c.execute('''
    CREATE TABLE Users (
        user_id INTEGER PRIMARY KEY,
        fname VARCHAR(50) NOT NULL,
        lname VARCHAR(50) NOT NULL,
        address VARCHAR(80) NOT NULL,
        email VARCHAR(50) NOT NULL
    )
''')

# Create Products table
c.execute('''
    CREATE TABLE Products (
        product_id INTEGER PRIMARY KEY,
        seller_id INTEGER,
        FOREIGN KEY(seller_id) REFERENCES Users(user_id),
        product_name VARCHAR(50) NOT NULL,
        starting_price DECIMAL NOT NULL,
        sale_date DATE NOT NULL,
        end_date DATE NOT NULL
    )
''')

# Create Bids table
c.execute('''
    CREATE TABLE Bids (
        bid_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(product_id),
        bidder_id INTEGER,
        FOREIGN KEY(bidder_id) REFERENCES Users(user_id),
        bid_amount DECIMAL,
        comments VARCHAR(100)
    )
''')

# Create Winners table
c.execute('''
    CREATE TABLE Winners (
        winner_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(product_id),
        bidder_id INTEGER,
        FOREIGN KEY(bidder_id) REFERENCES Users(user_id)
    )
''')

# Create Shipments table
c.execute('''
    CREATE TABLE Shipments (
        shipment_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(product_id),
        shipping_company VARCHAR(40),
        shipment_status VARCHAR(20)
    )
''')

# Create Payments table
c.execute('''
    CREATE TABLE Payments (
        payment_id INTEGER PRIMARY KEY,
        winner_id INTEGER,
        FOREIGN KEY(winner_id) REFERENCES Winners(winner_id),
        payment_amount DECIMAL,
        payment_date DATE
    )
''')

# Create Transactions table
c.execute('''
    CREATE TABLE Transactions (
        transaction_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(product_id),
        seller_id INTEGER,
        FOREIGN KEY(seller_id) REFERENCES Users(user_id),
        payment_id INTEGER,
        FOREIGN KEY(payment_id) REFERENCES Payments(payment_id),
        eBay_cut DECIMAL,
        seller_amount DECIMAL
    )
''')

# Insert data into Users table
c.execute('''
    INSERT INTO Users (fname, lname, address, email)
    VALUES
          ('Tyler', 'Durden', '1234 Dont talk about it ave', 'tdurden@fight.com'),
          ('Harvey', 'Specter', '1234 New York drive', 'hspecter@nyc.com'),
          ('Jesse', 'Pinkman', '1234 Albuquerque ave', 'jpinkman@walter.com')
''')

# Insert data into Products table
c.execute('''
    INSERT INTO Products (seller_id, product_name, starting_price, sale_date, end_date)
    VALUES
            (1, 'Soap', 1.00, '2019-01-01', '2019-01-31'),
            (2, 'Suit', 100.00, '2019-01-01', '2019-01-31'),
            (3, 'Blue Crystals', 1000.00, '2019-01-01', '2019-01-31')
''')

# Insert data into Bids table
c.execute('''
    INSERT INTO Bids (bid_id, product_id, bidder_id, bid_amount, comments)
    VALUES
          (2, 1, 2, 75, 'I want this soap'),
          (1, 3, 2, 21, 'I want this crystal'),
          (3, 2, 1, 90, 'I want this suit')
''')

# Insert data into Winners table
c.execute('''
    INSERT INTO Winners (winner_id, product_id, bidder_id)
    VALUES
            (1, 1, 2),
            (3, 3, 1),
            (2, 2, 3)
''')

# Insert data into Shipments table
c.execute('''
    INSERT INTO Shipments (shipment_id, product_id, shipping_company, shipment_status)
    VALUES
            (1, 1, 'USPS', 'Shipped'),
            (2, 2, 'UPS', 'Shipped'),
            (3, 3, 'FedEx', 'Shipped')
''')

# Insert data into Payments table
c.execute('''
    INSERT INTO Payments (payment_id, winner_id, payment_amount, payment_date)
    VALUES
            (1, 1, 75, '2019-01-01'),
            (2, 2, 90, '2019-01-01'),
            (3, 3, 21, '2019-01-01')
''')

# Insert data into Transactions table
c.execute('''
    INSERT INTO Transactions (transaction_id, product_id, seller_id, payment_id, eBay_cut, seller_amount)
    VALUES
            (2, 2, 2, 2, 11.93, 78.1),
          (3, 3, 1, 3, 2.78, 18.21),
          (1, 1, 3, 1, 9.93, 65.06)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
