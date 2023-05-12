# Create tables
customers_tbl = """ CREATE TABLE IF NOT EXISTS customers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name  TEXT,
    last_name     TEXT,
    postcode    TEXT ,
    house_number INTEGER,
    phone_number INTEGER
)"""

castles_tbl = """CREATE TABLE IF NOT EXISTS castles (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    dimensions TEXT,
    main_colour TEXT,
    name        TEXT,
    max_occupants INTEGER,
    hire_price INTEGER
)"""
booking_tbl ="""CREATE TABLE IF NOT EXISTS bookings (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    castle_id INTEGER,
    booking_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (castle_id) REFERENCES castles(id) ON DELETE CASCADE
);"""
