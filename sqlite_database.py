import sqlite3


class DB:

    def __init__(self):
        self.conn = sqlite3.connect('items.db')

        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS items (
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

    def insert(self, item_1):

        self.c.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (item_1.date, item_1.item_name,
                                                                                   item_1.item_number, item_1.details,
                                                                                   item_1.price, item_1.seller, item_1.buyer,
                                                                                   item_1.location, item_1.initials,
                                                                                   item_1.more_info))

        self.conn.commit()


    # returns items from database
    def read_from_db(self):
        self.c.execute('SELECT * FROM items')
        data = self.c.fetchall()
        for row in data:
            print(row)

    def close_conn(self):
        self.read_from_db()
        self.c.close()
        self.conn.close()
