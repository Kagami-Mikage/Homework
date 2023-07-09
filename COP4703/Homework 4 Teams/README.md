# Homework 4 - It Takes A Team

<p><b>Members</b></p>
<p><a href="https://github.com/ThurmondGuy">Thurmond Guy</a> - Database Modeler</p>
<p>Billy Huynh - Database Developer </p>
<p>Arnav Kadam - Database Administrator</p>
<p>Albert Kang - Database Architect</p>
<p>Michael Kelly - Database Engineer</p>
<p>Parker Kimbleton - Database Analyst</p>
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

# Normalization

<p>Normalization is a process in database design that helps organize and structure data in a relational database. It involves breaking down larger tables into smaller, more manageable tables and establishing relationships between them.</p>

<p>There are several normal forms with each of their own sets of rules and criteria:</p>

<ul>
    <li>First Normal Form (1NF): Attributes of a relation are atomic values and do not contain sets.</li>
    <li>Second Normal Form (2NF): Non-key attributes of a relational must be fully functionally dependent on a key.</li>
    <li>Third Normal Form (3NF): A functional dependency FD X → Y of a relation must have X as a candidate key or Y as part of a (possibly different) candidate key.</li>
    <li>Boyce-Codd Normal Form (BCNF): A functional dependency FD X → Y where X is a key of the relation.</li>
</ul>

# Database ER Model

# Creating the Relational Database in Oracle and Inserting a Sample Data Set

# Testing the Relational Database 

# Procedures, Stored Functions, & Triggers

<p><b>Scheduled Procedures:</n></p>

<p><b>Stored Functions:</b></p>

<p><b>Triggers:</b></p>




