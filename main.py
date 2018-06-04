import tkinter as tk
import sqlite_database as db


class Item:
    """Enter store items and details"""
    def __init__(self, date, item_name, item_number, location, details, price, seller, buyer, initials, more_info):
        self.date = date
        self.item_name = item_name
        self.item_number = item_number
        self.location = location
        self.details = details
        self.price = price
        self.seller = seller
        self.buyer = buyer
        self.initials = initials
        self.more_info = more_info


class EnterData:
    """screen 2"""
    def __init__(self, master):
        self.master = master
        # buttons
        tk.Button(master, text='Enter', command=self.enter).grid(row=10, column=1, sticky=tk.W, pady=4)
        tk.Button(master, text='Quit', command=master.destroy).grid(row=10, column=0, sticky=tk.W, pady=4)
        # label of input box
        tk.Label(master, text="Date").grid(row=0)
        tk.Label(master, text="Item").grid(row=1)
        tk.Label(master, text="Item Number").grid(row=2)
        tk.Label(master, text="Where").grid(row=3)
        tk.Label(master, text="Details").grid(row=4)
        tk.Label(master, text="Price").grid(row=5)
        tk.Label(master, text="Seller").grid(row=6)
        tk.Label(master, text="Buyer").grid(row=7)
        tk.Label(master, text="Initials").grid(row=8)
        tk.Label(master, text="More Info").grid(row=9)
        # input box
        self.date = tk.Entry(master)
        self.item_name = tk.Entry(master)
        self.item_number = tk.Entry(master)
        self.where = tk.Entry(master)
        self.details = tk.Entry(master)
        self.price = tk.Entry(master)
        self.seller = tk.Entry(master)
        self.buyer = tk.Entry(master)
        self.initials = tk.Entry(master)
        self.more_info = tk.Entry(master)
        # align input box
        self.date.grid(row=0, column=1)
        self.item_name.grid(row=1, column=1)
        self.item_number.grid(row=2, column=1)
        self.where.grid(row=3, column=1)
        self.details.grid(row=4, column=1)
        self.price.grid(row=5, column=1)
        self.seller.grid(row=6, column=1)
        self.buyer.grid(row=7, column=1)
        self.initials.grid(row=8, column=1)
        self.more_info.grid(row=9, column=1)

    def enter(self):
        self.item = Item(self.date.get(),
                         self.item_name.get(),
                         self.item_number.get(),
                         self.where.get(),
                         self.details.get(),
                         self.price.get(),
                         self.seller.get(),
                         self.buyer.get(),
                         self.initials.get(),
                         self.more_info.get()
                         )
        sql = db.DB()
        sql.insert(self.item)
        sql.close_conn()


class List:
    """screen 1"""
    def __init__(self, master):
        self.master = master

        # creates grid
        height = 20
        width = 10
        for i in range(height):  # rows
            for j in range(width):  # columns
                b = tk.Entry(master, text='')
                b.grid(row=i, column=j)
                tk.Button(master, text='Add Item', command=self.add_item).grid(row=20, column=1,
                                                                                             sticky=tk.W, pady=4)
                tk.Button(master, text='   Edit   ', command=self.edit_item).grid(row=20, column=0,
                                                                                                sticky=tk.E, pady=4)
                tk.Label(master, text="Date", padx=60).grid(row=0, column=0, pady=4)
                tk.Label(master, text="Item", padx=60).grid(row=0, column=1, pady=4)        # might have to do 'self.date_label = tk.label(...)'
                tk.Label(master, text="Item Number", padx=35).grid(row=0, column=2, pady=4) # self.date_label.grid(...)
                tk.Label(master, text="Where", padx=60).grid(row=0, column=3, pady=4)       # to reference specific grid when
                tk.Label(master, text="Details", padx=60).grid(row=0, column=4, pady=4)     # fetching data from it
                tk.Label(master, text="Price", padx=60).grid(row=0, column=5, pady=4)
                tk.Label(master, text="Seller", padx=60).grid(row=0, column=6, pady=4)
                tk.Label(master, text="Buyer", padx=60).grid(row=0, column=7, pady=4)
                tk.Label(master, text="Initials", padx=60).grid(row=0, column=8, pady=4)
                tk.Label(master, text="More Info", padx=50).grid(row=0, column=9, pady=4)

    def add_item(self):
        self.addItem = tk.Toplevel(self.master)
        self.app = EnterData(self.addItem)

    def edit_item(self):
        self.editItem = tk.Toplevel(self.master)
        self.app = EnterData(self.editItem)


def main():
    root = tk.Tk()
    app = List(root)
    root.mainloop()


if __name__ == '__main__':
    main()
