import sqlite3
from main import Item

conn = sqlite3.connect('items.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS items (
            date text,
            item_name text,
            item_number text,
            details text,
            price real,
            seller text,
            buyer text,
            location text,
            initials text,
            more_info text
            )""")

item_1 = Item()

c.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (item_1.date, item_1.item_name, item_1.item_number,
                                                                   item_1.details, item_1.price, item_1.seller,
                                                                   item_1.buyer, item_1.location, item_1.initials,
                                                                   item_1.more_info))


print(c.fetchall())

conn.commit()
c.close()
conn.close()
