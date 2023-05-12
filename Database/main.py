import sqlite3 as db
import pandas as pd
import functions as func


conn = db.connect("mycastleDB.db")
cur = conn.cursor()
func.initatedb()

operation = input("What CRUD operation would you like to execute? (Create = 1, Read = 2, Update = 3, Delete = 4) - ")

# Create of CRUD
if operation == "1":
    action = input("\nPress 1 to add a new customer, 2 to add a new castle, 3 to add new booking - ")
    if action == "1":
            func.addToCustomer(cur)
            conn.commit()

    elif action == "2" :
            func.addToCastle(cur)
            conn.commit()

    elif action == "3":
            func.addToBooking(cur)
            conn.commit()
    else:
        print("You have not chosen a table to add new booking")


# Read of CRUD
if operation == "2":
    table_sel = input("\nWhat table would you like to read from? (customers = 1 , castles = 2, bookings = 3) - ")
    if table_sel == "1": table = "customers"
    elif table_sel == "2": table = "castles"
    elif table_sel == "3": table = "bookings"
    else: print("You have not selected a table")

    if table == "customers": table_col = ["ID", "first_name", "last_name", "postcode", "house_number", "phone_number"]
    elif table == "castles": table_col = ["ID", "dimensions", "main_colour", "name", "max_occupants", "hire_price"]
    else: table_col = ["ID", "customer_id", "castle_id", "booking_date"]

    selector = input("Would you like to search for a single value or select all values? (All = 1, Single = 2) - ")
    if selector == "1":
        sql_query = pd.read_sql(f"SELECT * FROM {table}", conn)
        dataframe = pd.DataFrame(sql_query, columns = table_col)
        print(dataframe)

    elif selector == "2":
        id = input(f"What is the {table} ID? - ")
        sql_query = pd.read_sql(f"SELECT * FROM {table} WHERE id={id}", conn)
        dataframe = pd.DataFrame(sql_query, columns = table_col)
        print(dataframe)

    else:
        print("You have not selected All values or Single Value")

# Update of CRUD
if operation == "3":
    table_sel = input("What table would you like to update a value from? (customers = 1, castles = 2, bookings = 3) - ")
    if table_sel == "1":
        id = input("What is the ID of the value you want to update? - ")
        func.update_customer(id, cur)
        conn.commit()

    elif table_sel == "2":
        id = input("What is the ID of the value you want to update? - ")
        func.update_castle(id, cur)
        conn.commit()

    elif table_sel == "3":
        id = input("What is the ID of the value you want to update? - ")
        func.update_booking(id, cur)
        conn.commit()

    else:
        print("You have not selected a table to update a value")

# Delete of CRUD
if operation == "4":
    table_sel = input("What table would you like to delete a value from? (customers = 1, castles = 2, bookings = 3) - ")
    if table_sel == "1":
        func.delete_customer(cur)
        conn.commit()

    elif table_sel == "2":
        id = input("What is the ID of the value you want to delete? - ")
        func.delete_castle(id, cur)
        conn.commit()

    elif table_sel == "3":
        id = input("What is the ID of the value you want to delete? - ")
        func.delete_booking(id, cur)
        conn.commit()

    else:
        print("You have not selected a table to delete a value")

conn.close()
