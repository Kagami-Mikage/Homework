# Homework 4 - It Takes A Team

<p><b>Members</b></p>
<p><a href="https://github.com/ThurmondGuy">Thurmond Guy</a> - Database Modeler</p>
<p>Billy Huynh - Database Analyst</p>
<p>Arnav Kadam - Database Administrator</p>
<p>Albert Kang - Database Architect</p>
<p>Michael Kelly - Database Engineer</p>
<p>Parker Kimbleton - Database Developer</p>
<p>Joshua Marquez - Database Tester</p>

<p><b>Other Versions</b></p>
<p><a href="https://usfedu-my.sharepoint.com/:p:/g/personal/tandrino_usf_edu/EarQ7FlqVn9Mpropt1UxpIgBlKjtdUmcHh4eJwpqoMGsRA?e=UQ702V">PowerPoint Presentation</p></a>

# Background
<p align="justify">In this group project each member of the team will play a different, but interconnected, role. The seven 
roles are as follows: <b>Database Administrator, Database Developer, Database Tester, Database Analyst, 
Database Engineer, Database Architect, and Database Modeler.</b> It is the responsibility of the team to assign one role to each member of the team.</p>

<p align="justify">Your team has been assigned a scenario. The scenario description that you have been given does not contain enough information for your team to complete this task. This means that the team is going to have to be responsible for filling in the gaps. The team will perform the following steps:</p>

<ol type="1">
    <li>
        <p><b>The Database Administrator</b> will be responsible for describing the database that the team decided to create. This will include listing out the tables that were created, the rows and columns that the tables contain, any indexes that the team decided to create to speed things up, and any views that were created.
        </p>
    </li>
    <li>
        <p><b>The Database Developer</b> will need to determine what types of processing will be needed by the customer that the DBMS will not be able to provide. They will need to document what data they will need to extract from the database and what they will then do with that data. They will also have to describe what data they will be adding to the database and what data they will be modifying.
        </p>
    </li>
    <li>
        <p><b>The Database Tester</b> will describe their plans for maintaining database integrity and how they would go about testing the database and handling temporal data.
        </p>
    </li>
    <li>
        <p><b>The Database Analyst</b> will determine what scheduled procedures, stored functions, and triggers will be required. They will then define them.
        </p>
    </li>
    <li>
        <p><b>The Database Engineer</b> will explain how the team's database was normalized. They will also lay out the various joins that will be required in order to extract the required data from the database.
        </p>
    </li>
    <li>
        <p><b>The Database Architect</b> will work with the database modeler to create a design via the ER model following the 8 steps that we covered in class. 
        </p>
    </li>
    <li>
        <p><b>The Database Modeler</b> will create an Entity–relationship diagram to show the layout of the team's proposed database design. They will be responsible for creating an ER diagram of the database that the team decides to build. The entities, attributes, relationships, and degree of relationships will all have to be defined. 
        </p>
    </li>
</ol>

<p align="justify">Your team is required to implement the database that you design in an <b>Orcal 19c database</b> (<a href="https://livesql.oracle.com">https://livesql.oracle.com</a>). Keep in mind that every SQL command that you use to create your database, load it with data, or create stored procedures can be saved in a text file and shared with other team members so that everyone can replicate the same database</p>

# Scenario #4: eBay

<p align="justify">It turns out that running the world's largest online auction is a tough job. You have agreed to help eBay out by creating a new database for them that they will be able to use to keep track of all of the sales that they have going on. </p>

<p align="justify">Your database is going to have to keep track of everyone who has an eBay account. These people have a name, address, and email. They can post items that they want to sell. You will need to keep track of every sale: what is being sold, how much is its starting price, what date did it go on sale, how long will the sale last?</p>

<p align="justify">Each time a customer makes a bid, your data base will need to keep track of the bid: how much bid, who bid it, any comments? Once the bidding is over, your database will have to allow the person who posted the product to determine who posted the winning bid. </p>

<p align="justify">The seller will have to get in touch with the bidder and inform them that they won. The winner will have to confirm that they want the product. The seller will then have to package and ship the 
product to the winner. </p>

<p align="justify">While the product is in transit, the winner needs to be able to determine what company was 
used to ship the product and what the current status of the product is.</p>

<p align="justify">eBay will need to collect the money from the winner and then, after taking its cut, will need to 
make sure that the rest of the money is given to the person who sold the product.</p>

# Functional Dependencies
<p><b>Entities and Attributes</b></p>
<p>Users (UserID, Name, Address, Email)</p>
<p>Products (ProductID, Name, Description, StartingPrice, DateOnSale, SaleLength)</p>
<p>Bids (BidID, UserID, ProductID, Amount, Comments)</p>
<p>Winners (UserID, ProductID)</p>
<p>Shipping (UserID, ProductID, Company, Status)</p>
<p>Payments (UserID, ProductID, Amount)</p>

<p><b>Functional Dependencies</b></p>
<p>UserID → Name, Address, Email</p>
<p>ProductID → Name, Description, StartingPrice, DateOnSale, SaleLength</p>
<p>BidID → UserID, ProductID, Amount, Comments</p>
<p>UserID, ProductID → Company, Status</p>
<p>UserID, ProductID → Amount</p>

<p><b>Relationships</b></p>
<p>All of our tables have a 1:M relationship between another tbale</p>
<p>Users 1:M Bids, Products, Transactions, Winners</p>
<p>Products 1:M Bids, Transactions, Winners</p>
<p>Payments 1:M Transactions</p>
<p>Winners 1:M Payments</p>

# Normalization

<p>Normalization is a process in database design that helps organize and structure data in a relational database. It involves breaking down larger tables into smaller, more manageable tables and establishing relationships between them.</p>

<p>There are several normal forms with each of their own sets of rules and criteria:</p>

<ul>
    <li>First Normal Form (1NF): Attributes of a relation are atomic values and do not contain sets.</li>
    <li>Second Normal Form (2NF): Non-key attributes of a relational must be fully functionally dependent on a key.</li>
    <li>Third Normal Form (3NF): A functional dependency FD X → Y of a relation must have X as a candidate key or Y as part of a (possibly different) candidate key.</li>
    <li>Boyce-Codd Normal Form (BCNF): A functional dependency FD X → Y where X is a key of the relation.</li>
</ul>

<p>All the tables in the database follow the rules to be in 1NF which are: 2D rows and columns, each row containing data to something, each column pertaining to a single attribute, each cell has only one value, entries in a column must all be the same kind, each column is unique in name, no row is identical to another, and the order is not significant.</p>

<p>Since we are keeping track of all the Users, Products, Bids, Winners, Payments, Shipments, and Transactions it would be best to keep them in separate tables to remove the possibility of transitive dependencies, so if something needed to be removed for example if a transaction was cancelled, the User and the Product tables would be fine, and the transaction would just be removed.</p>

<p>The standard for this database is 3NF due to removing transitive dependencies, having functional dependency, and for following the criteria of 1NF.</p>



# Database ER Model

<img src="https://github.com/ThurmondGuy/Homework/blob/main/COP4703/Homework%204%20Teams/ER%20MODEL/ebay.png">

<p>Created with <a href="https://dbdiagram.io/d">dbdiagram.io</a>. Check <a href="https://github.com/ThurmondGuy/Homework/blob/main/COP4703/Homework%204%20Teams/ER%20MODEL/ebay.dbml">ebay.dbml</a> for the code.</p>

# Creating the Relational Database in Oracle and Inserting a Sample Data Set

Database tables have been created from the relational schema in Oracle SQL Developer with SQL `CREATE TABLE` and `INSERT` statements. Sample data has been created and inserted into these tables to allow for realistc taesting. The method used to create the tables and sample data is described in this python <a href="https://github.com/ThurmondGuy/Homework/blob/main/COP4703/Homework%204%20Teams/SQL%20code/ebay.py">file</a>.

<p>Below here are the statements used to create the tables. To see the database file with the sample data, <a href="https://github.com/ThurmondGuy/Homework/blob/main/COP4703/Homework%204%20Teams/SQL%20code/database.db">click here</a>.</p>

<p><i>Users Table</i></p>

```sql
CREATE TABLE Users (
        user_id INTEGER PRIMARY KEY,
        fname VARCHAR(50) NOT NULL,
        lname VARCHAR(50) NOT NULL,
        address VARCHAR(80) NOT NULL,
        email VARCHAR(50) NOT NULL
);

INSERT INTO Users (fname, lname, address, email)
    VALUES
          ('Tyler', 'Durden', '1234 Dont talk about it ave', 'tdurden@fight.com'),
          ('Harvey', 'Specter', '1234 New York drive', 'hspecter@nyc.com'),
          ('Jesse', 'Pinkman', '1234 Albuquerque ave', 'jpinkman@walter.com')
;
```

<p><i>Products Table</i></p>

```sql
CREATE TABLE Products (
        product_id INTEGER PRIMARY KEY,
        seller_id INTEGER,
        FOREIGN KEY(seller_id) REFERENCES Users(user_id),
        product_name VARCHAR(50) NOT NULL,
        starting_price DECIMAL NOT NULL,
        sale_date DATE NOT NULL,
        end_date DATE NOT NULL
);
INSERT INTO Products (seller_id, product_name, starting_price, sale_date, end_date)
    VALUES
            (1, 'Soap', 1.00, '2019-01-01', '2019-01-31'),
            (2, 'Suit', 100.00, '2019-01-01', '2019-01-31'),
            (3, 'Blue Crystals', 1000.00, '2019-01-01', '2019-01-31')
;
```

<p><i>Bids Table</i></p>

```sql
CREATE TABLE Bids (
        bid_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(product_id),
        bidder_id INTEGER,
        FOREIGN KEY(bidder_id) REFERENCES Users(user_id),
        bid_amount DECIMAL,
        comments VARCHAR(100)
);

INSERT INTO Bids (bid_id, product_id, bidder_id, bid_amount, comments)
    VALUES
          (2, 1, 2, 75, 'I want this soap'),
          (1, 3, 2, 21, 'I want this crystal'),
          (3, 2, 1, 90, 'I want this suit')
;
```

<p><i>Winners Table</i></p>

```sql
CREATE TABLE Winners (
        winner_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(product_id),
        bidder_id INTEGER,
        FOREIGN KEY(bidder_id) REFERENCES Users(user_id)
);

INSERT INTO Winners (winner_id, product_id, bidder_id)
    VALUES
            (1, 1, 2),
            (3, 3, 1),
            (2, 2, 3)
;
```

<p><i>Shipping Table</i></p>

```sql
CREATE TABLE Shipments (
        shipment_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES Products(product_id),
        shipping_company VARCHAR(40),
        shipment_status VARCHAR(20)
);

INSERT INTO Shipments (shipment_id, product_id, shipping_company, shipment_status)
    VALUES
            (1, 1, 'USPS', 'Shipped'),
            (2, 2, 'UPS', 'Shipped'),
            (3, 3, 'FedEx', 'Shipped')
;
```

<p><i>Payments Table</i></p>

```sql
CREATE TABLE Payments (
        payment_id INTEGER PRIMARY KEY,
        winner_id INTEGER,
        FOREIGN KEY(winner_id) REFERENCES Winners(winner_id),
        payment_amount DECIMAL,
        payment_date DATE
);

INSERT INTO Payments (payment_id, winner_id, payment_amount, payment_date)
VALUES
        (1, 1, 75, '2019-01-01'),
        (2, 2, 90, '2019-01-01'),
        (3, 3, 21, '2019-01-01')
;
```

<p><i>Transactions Table</i></p>

```sql
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
);

INSERT INTO Transactions (transaction_id, product_id, seller_id, payment_id, eBay_cut, seller_amount)
    VALUES
            (2, 2, 2, 2, 11.93, 78.1),
          (3, 3, 1, 3, 2.78, 18.21),
          (1, 1, 3, 1, 9.93, 65.06)
;
```

# Testing the Relational Database 
<h3>Database Tester</h3>
<p><b>Primary Role</b>:Validating the functionality, efficiency, reliability, & security of our team's designed database, ensuring data accuracy & performance consistency througha  structured testing process.</p>

<p><b>Develop a well-designed database</b></p>
<ul>
    <li>Design a thorough database schema</li>
    <li>Validate for normalization to avoid data redundancy</li>
    <li>Optimize for swift and efficient data storage and retrieval</li>
</ul>

<p><b>Maintaining Integrity & Functionality</b></p>
<ul>
    <li>Deploy robust checks to uphold precision in data</li>
    <li>Implement input validation to protect against data inconsistencies and anomalies</li>
    <li>Devise thorough test plans and cases aimed at certifying the desired functionality of the database</li>
    <li>Ensure testing is comprehensive</li>
</ul>

<p><b>Security Plan</b></p>
<ul>
    <li>Conduct internal and external penetration testing and follow recommendations to further secure the database security</li>
</ul>

<p><b>How will we handle temporary data?</b></p>
<ul>
    <li>Recognize unique requirements of temporal data</li>
    <li>Confirm uniform handling across various time scenarios</li>
    <li>Access system handling under heavy temporal data load</li>
    <li>Check backup  and restoration effectiveness for temporal data</li>
</ul>

<p>Here are some sample code snippets of our testing:</p>

<p><b>Testing the database connection</b></p>

```sql
SELECT * FROM Users;
```

<p><b>Testing the data insertion</b></p>

```sql
INSERT INTO Users (user_id, fname, lname, address, email)
    VALUES
            (4, 'John', 'Doe', '1234 Main St', 'john@aol.com')
;
```

<p><b>Testing the data deletion</b></p>

```sql
DELETE FROM bids WHERE bid_id = 4;
```

<p><b>Testing the data update</b></p>

```sql
UPDATE bids SET bid_amount = 200 WHERE bid_id = 3;
```

<p><b>Testing the data retrieval</b></p>

```sql
SELECT * FROM bids WHERE bid_id = 3;
```

<p><b>Which customer made the highest bid?</b></p>

```sql
SELECT MAX(bid_amount) FROM bids;
```

<p><b>Average bid amount?</b></p>

```sql
SELECT AVG(bid_amount) FROM bids;
```

<p><b>When will the auction end?</b></p>

```sql
SELECT end_date FROM Products;
```

<p><b>How many bids were made on the date of 2019-01-01?</b></p>

```sql
SELECT COUNT(bid_id) FROM bids WHERE bid_date = '2019-01-01';
```
<p><b>What shipping supplier had the most shipments?</b></p>

```sql
SELECT shipping_company, COUNT(shipment_id) FROM Shipments GROUP BY shipping_company;
```

# Procedures, Stored Functions, & Triggers

<p><b>Scheduled Procedures:</b></p>
<p>ShowCurrentBidAmount: Display the current bid amount on an item (bid_amount).</p>

<p>ShowWinnerInformation: Display the winner information (winner_id.)</p>

<p>UpdatePersonalInfo: Allow user to update personal information.</p>

<p><b>AddInBid</b>: Procedure to add in new bids. (Insert into Bids).</p>

<p>MarkComplete: If the auction needs to end (Someone made an offer you cannot refuse).</p>

<p>DisplayAuctionStatus: Ended or In Progress.</p>

<p><b>Stored Functions:</b></p>

<p><b>GetShippingCost</b>: Given a customer zip code, calculate the shipping cost.</p>

<p>Get(Average)(Lower)(Highest)BidAmount: Calculate / get the appropriate bid amount for the user.</p>

<p>CountActiveAuctions: Return the number of auctions that a user has.</p>

<p>CheckBid: Check if the bid is valid (compare the current bid amount with the highest bid amount. If lower, return this bid is not valid, else bid is valid).</p>

<p>Get(Seller)(User)Rating: Get the user or seller rating by calculating the averages of the ratings.</p>

<p>GetFees: Calculate the fees the seller pay eBay by taking winning bid amount and deduct a percentage from it. Return the deducted amount.</p>

<p>GetDuration: Calculate the average duration of all the auction the seller hosted. Or a single auction.</p>

<p>GetRevenge: Return the total amount  of money that will be tranfered to the seller bank account (or externally).</p>

<p><b>Triggers:</b></p>

<p><b>AfterAuctionCompletion</b>: A trigger when the duration of the auction is over. Send a notification to the winner and seller. As well as to the losing bid user.</p>

<p>AfterBid: A trigger when a new bid has been inserted.</p>

<p>Winner: A trigger when the auction expires, highest bid amound user will be the winner.</p>

<p>WarningAuctionNoTime: A trigger to remind the user that the auction is ending in 30 minutes.</p>

<p>TriggerAfterProductShip: A trigger after the product has been shipped.</p>

<hr>
<p>After creating the sets of required procedures, stored functions and triggers, a database analyst would use the feedback from the user to update(add/remove) current sets accordingly.</p>

# Implementation (Oracle 19c)
<p>Sample Implementation of a Procedure, Trigger, and a Function.</p>

<p>Procedure: AddInBid</p>

```sql
CREATE OR REPLACE PROCEDURE AddInBid
    (param_ product_id IN INT, p_bidder_id IN INT,
    p_bid_amount IN DECIMAL, p_comments IN VARCHAR)
AS
BEGIN
    INSERT INTO Bids(bid_id, 
    product_id, bid_amount, comments)
    VALUES(bid_id_sequence NEXTVAL, p.product_id, 
    p.bidder_id, p.bid_amount, p.comments);
COMMIT; - Commit the transaction
```

<p>Trigger: AfterAuctionCompletion</p>

```sql
CREATE OR REPLACE TRIGGER AfterAuctionCompletion
AFTER UPDATE OF end_date ON Products
FOR EACH ROW
BEGIN
    IF NEW end_date = SYSDATE THEN
        INSERT INTO Notifications(notification_id, 
        user_id, message, notification_date)
        VALUES(notification_id_sequence NEXTVAL, 
        p.user_id, 'Auction has ended', SYSDATE);
    END IF;
    NULL; 
END IF;
END;
```

<p>Function: GetShippingCost</p>

```sql
CREATE OR REPLACE FUNCTION GetShippingCost
    (p_zip_code IN VARCHAR)
RETURN DECIMAL
AS
    v_shipping_cost DECIMAL;
BEGIN
    IF p_zip_code = '33620' THEN
        v_shipping_cost := 5.00;
    ELSE
        v_shipping_cost := 10.00;
    END IF;
    RETURN v_shipping_cost;
END;
```



