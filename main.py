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
        self.button = tk.Button(master, text='Enter', command=self.enter).grid(row=10, column=1, sticky=tk.W, pady=4)
        self.button = tk.Button(master, text='Quit', command=master.destroy).grid(row=10, column=0, sticky=tk.W, pady=4)
        # label of input box
        self.label = tk.Label(master, text="Date").grid(row=0)
        self.label = tk.Label(master, text="Item").grid(row=1)
        self.label = tk.Label(master, text="Item Number").grid(row=2)
        self.label = tk.Label(master, text="Where").grid(row=3)
        self.label = tk.Label(master, text="Details").grid(row=4)
        self.label = tk.Label(master, text="Price").grid(row=5)
        self.label = tk.Label(master, text="Seller").grid(row=6)
        self.label = tk.Label(master, text="Buyer").grid(row=7)
        self.label = tk.Label(master, text="Initials").grid(row=8)
        self.label = tk.Label(master, text="More Info").grid(row=9)
        # input box
        self.date = tk.Entry(master)
        self.item = tk.Entry(master)
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
        self.item.grid(row=1, column=1)
        self.item_number.grid(row=2, column=1)
        self.where.grid(row=3, column=1)
        self.details.grid(row=4, column=1)
        self.price.grid(row=5, column=1)
        self.seller.grid(row=6, column=1)
        self.buyer.grid(row=7, column=1)
        self.initials.grid(row=8, column=1)
        self.more_info.grid(row=9, column=1)

    # enter data
    def enter(self):
        print(self.date.get())



class List:
    """screen 1"""
    def __init__(self, master):
        self.master = master

        # creates grid
        height = 20
        width = 10
        for i in range(height):  # rows
            for j in range(width):  # columns
                self.button = tk.Button(master, text='Add Item', command=self.add_item).grid(row=20, column=1,
                                                                                             sticky=tk.W, pady=4)
                b = tk.Entry(master, text='')
                b.grid(row=i, column=j)

    def add_item(self):
        self.addItem = tk.Toplevel(self.master)
        self.app = EnterData(self.addItem)


def main():
    root = tk.Tk()
    app = List(root)
    root.mainloop()


if __name__ == '__main__':
    main()
