import sqlite3

conn = sqlite3.connect('Getting_Help.db')

c = conn.cursor()

drop_hotel = '''DROP TABLE IF EXISTS Hotel'''
c.execute(drop_hotel)
drop_room_availability = '''DROP TABLE IF EXISTS RoomAvailability'''
c.execute(drop_room_availability)
drop_room = '''DROP TABLE IF EXISTS Room'''
c.execute(drop_room)
drop_point_of_interest = '''DROP TABLE IF EXISTS PointOfInterest'''
c.execute(drop_point_of_interest)
drop_hotel_to_poi = '''DROP TABLE IF EXISTS HotelToPOI'''
c.execute(drop_hotel_to_poi)
drop_reservation = '''DROP TABLE IF EXISTS Reservation'''
c.execute(drop_reservation)
drop_guest = '''DROP TABLE IF EXISTS Guest'''
c.execute(drop_guest)
drop_room_to_amenity = '''DROP TABLE IF EXISTS RoomToAmenity'''
c.execute(drop_room_to_amenity)
drop_amenity = '''DROP TABLE IF EXISTS Amenity'''
c.execute(drop_amenity)

def create_tables():
    c.execute('''CREATE TABLE Hotel (
                    hotelid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL
                )''')
    
    c.execute('''CREATE TABLE RoomAvailability(
                    roomid INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotelid INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    available TEXT NOT NULL,
                    FOREIGN KEY (hotelid) REFERENCES Hotel(hotelid)
                )''')
    
    c.execute('''CREATE TABLE Room(
                    roomid INTEGER PRIMARY KEY AUTOINCREMENT,
                    hotelid INTEGER NOT NULL,
                    roomNumber INTEGER NOT NULL,
                    rate REAL NOT NULL,
                    FOREIGN KEY (hotelid) REFERENCES Hotel(hotelid)
                )''')
    
    c.execute('''CREATE TABLE PointOfInterest(
                    poiid INTEGER PRIMARY KEY AUTOINCREMENT,
                    poiname TEXT NOT NULL,
                    poidescription TEXT NOT NULL
                )''')
    
    c.execute('''CREATE TABLE HotelToPOI(
                    hotelid INTEGER NOT NULL,
                    poiid INTEGER NOT NULL,
                    FOREIGN KEY (hotelid) REFERENCES Hotel(hotelid),
                    FOREIGN KEY (poiid) REFERENCES PointOfInterest(poiid)
                )''')
    
    c.execute('''CREATE TABLE Reservation(
                    reservationid INTEGER PRIMARY KEY AUTOINCREMENT,
                    guestid INTEGER NOT NULL,
                    roomid INTEGER NOT NULL,
                    startdate TEXT NOT NULL,
                    enddate TEXT NOT NULL,
                    confirmnumber TEXT NOT NULL,
                    FOREIGN KEY (guestid) REFERENCES Guest(guestid),
                    FOREIGN KEY (roomid) REFERENCES Room(roomid)
                )''')
    
    c.execute('''CREATE TABLE Guest(
                    guestid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')
    
    c.execute('''CREATE TABLE RoomToAmenity(
                    roomid INTEGER NOT NULL,
                    amenityid INTEGER NOT NULL
                )''')
    
    c.execute('''CREATE TABLE Amenity(
                    amenityid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )''')
    
def insert_data():
    c.execute('''INSERT INTO Hotel (name, phone, address)
                VALUES ('Happy Trails', '8135551234', '1234 Happy Trail Lane')
                ''')
    
    c.execute('''INSERT INTO RoomAvailability (hotelid, date, available)
                VALUES (1, '2023-06-22', True),
                (1, '2023-06-23', True),
                (1, '2023-06-24', True),
                (1, '2023-06-21', True)
                ''')

    c.execute('''INSERT INTO Room (hotelid, roomNumber, rate)
                VALUES (1, 100, 100.75),
                (1, 200, 200.5),
                (1, 300, 175.25),
                (1, 400, 110.5)
                ''')
    
    c.execute('''INSERT INTO PointOfInterest (poiname, poidescription)
                VALUES ('Ruby Falls', 'Attractive waterfall located close to hotel'),
                ('Happy Mall', 'Full service mall'),
                ('Ball Of String', 'Largest ball of string in the state')
                ''')
    
    c.execute('''INSERT INTO HotelToPOI (hotelid, poiid)
                VALUES (1, 1),
                (1, 2),
                (1, 3)
                ''')
    
    c.execute('''INSERT INTO Reservation (guestid, roomid, startdate, enddate, confirmnumber)
                VALUES (1, 4, '2023-05-29', '2023-06-02', '100'),
                (2, 3, '2023-05-29', '2023-06-02', '200'),
                (3, 2, '2023-05-29', '2023-06-02', '300'),
                (4, 1, '2023-05-29', '2023-06-02', '400')
                ''')
    
    c.execute('''INSERT INTO Guest (name, email)
                VALUES ('Bob Johson', 'bob@aol.com'),
                ('Ann Majors', 'ann@verizon.net'),
                ('Peter Jenkins', 'peter@comcast.com'),
                ('Mary Jenkins', 'mary@compuserve.com')
                ''')
    
    c.execute('''INSERT INTO RoomToAmenity (roomid, amenityid)
                VALUES (1, 1),
                (2, 3),
                (3, 2),
                (4, 1)
                ''')
    
    c.execute('''INSERT INTO Amenity (name)
                VALUES ('Hot Tub'),
                ('Tropical Shower'),
                ('Towel Warmer'),
                ('Nightly box of chocolates')
                ''')


def get_help():
    create_tables()
    insert_data()
    c.execute('''SELECT * FROM Hotel''')
    print("Hotel Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM RoomAvailability''')
    print("\nRoomAvailability Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM Room''')
    print("\nRoom Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM PointOfInterest''')
    print("\nPointOfInterest Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM HotelToPOI''')
    print("\nHotelToPOI Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM Reservation''')
    print("\nReservation Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM Guest''')
    print("\nGuest Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM RoomToAmenity''')
    print("\nRoomToAmenity Table:")
    for row in c.fetchall():
        print(row)

    c.execute('''SELECT * FROM Amenity''')
    print("\nAmenity Table:")
    for row in c.fetchall():
        print(row)

if __name__ == '__main__':
    get_help()
    conn.commit()
    conn.close()
    