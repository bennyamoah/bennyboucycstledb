import queries as q
import sqlite3 as db

def initatedb():
    connection = db.connect("mycastleDB.db")
    cursor  = connection.cursor()
    cursor.execute(q.booking_tbl)
    cursor.execute(q.customers_tbl)
    cursor.execute(q.castles_tbl)
    connection.commit()

# functions for adding data

# Adding Values to Customers
def addToCustomer(cursor):
    query = "INSERT INTO customers (first_name, last_name, postcode, house_number, phone_number) VALUES (?, ?, ?, ?, ?)"
    first_name= input( "First name: ")
    last_name = input("last name: ")
    postcode = input("postcode: ")
    house_number = int(input("house number: "))
    phone_number = int(input ("phone number: "))
    values = (first_name, last_name, postcode, house_number, phone_number)
    cursor.execute(query, values)

# Adding values to Castles
def addToCastle(cursor):
    query = "INSERT INTO castles (dimensions, main_colour, name, max_occupants, hire_price) VALUES (?, ?, ?, ?, ?)"
    dimensions = input( "dimensions: ")
    main_colour= input ("color: ")
    name= input("name: ")
    max_occupants = input("Max Occupancy: ")
    hire_price = int(input("price: "))
    values = (dimensions, main_colour, name, max_occupants ,hire_price)
    cursor.execute(query, values)

# Adding Values to Booking
def addToBooking(cursor):
    query = "INSERT INTO bookings (customer_id, castle_id, booking_date) VALUES (?, ?, ?)"
    customer_id = int(input ("customer id number: "))
    castle_id = int(input("castle id: "))
    booking_date = input ("date: ")
    values = (castle_id, customer_id, booking_date)
    cursor.execute(query, values)

# Functions to Update values

# Updating Value in Customers
def update_customer(customer_id, cursor):
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    new_postcode = input("Postcode: ")
    new_house_number = input("House Number: ")
    new_phone_number = input("Phone Number: ")
    cursor.execute("UPDATE customers SET first_name=?, last_name=?, postcode=?, house_number=?, phone_number=? WHERE id=?", (f_name, l_name, new_postcode, new_house_number, new_phone_number, customer_id))

# Updating Value in Castles
def update_castle(castle_id, cursor):
    new_dimensions = input("Dimensions: ")
    new_main_colour = input("Color: ")
    new_name = input("Name: ")
    new_max_occupants = input("Max Occupancy: ")
    new_hire_price = int(input("Price: "))
    cursor.execute("UPDATE castles SET dimensions=?, main_colour=?, name=?, max_occupants=?, hire_price=? WHERE id=?", (new_dimensions, new_main_colour, new_name, new_max_occupants, new_hire_price, castle_id))

# Updating Value in Booking
def update_booking(booking_id, cursor):
    nw_customer_id = int(input("New Customer ID: "))
    nw_castle_id = int(input("New Castle ID: "))
    nw_booking_date = input("New Date: ")
    cursor.execute("UPDATE bookings SET customer_id=?, castle_id=?, booking_date=? WHERE id=?", (nw_customer_id, nw_castle_id, nw_booking_date, booking_id))

# Functions to delete values

# Deleting a value in Customers
def delete_customer(cursor):
    customer_id = input("What is the ID of the customer you would like to delete? - ")
    cursor.execute("DELETE FROM customers WHERE id=?", (customer_id))

# Deleting a value in Castle
def delete_castle(cursor):
    castle_id = input("What is the ID of the castle you would like to delete? - ")
    cursor.execute("DELETE FROM castles WHERE id=?", (castle_id))

# Deleting a value in Booking
def delete_booking(cursor):
    booking_id = input("What is the ID of the booking you would like to delete? - ")
    cursor.execute("DELETE FROM bookings WHERE id=?", (booking_id))


