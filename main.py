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
        self.button = tk.Button(master, text='Quit', command=master.quit).grid(row=10, column=0, sticky=tk.W, pady=4)
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
        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)
        self.e3 = tk.Entry(master)
        self.e4 = tk.Entry(master)
        self.e5 = tk.Entry(master)
        self.e6 = tk.Entry(master)
        self.e7 = tk.Entry(master)
        self.e8 = tk.Entry(master)
        self.e9 = tk.Entry(master)
        self.e10 = tk.Entry(master)
        # align input box
        self.e1 = self.e1.grid(row=0, column=1)
        self.e2 = self.e2.grid(row=1, column=1)
        self.e3 = self.e3.grid(row=2, column=1)
        self.e4 = self.e4.grid(row=3, column=1)
        self.e5 = self.e5.grid(row=4, column=1)
        self.e6 = self.e6.grid(row=5, column=1)
        self.e7 = self.e7.grid(row=6, column=1)
        self.e8 = self.e8.grid(row=7, column=1)
        self.e9 = self.e9.grid(row=8, column=1)
        self.e10 = self.e10.grid(row=9, column=1)

    # enter data
    def enter(self):
        self.e1text = tk.StringVar()
        self.e1 = tk.Entry(self.master, textvariable=self.e1text)
        print(self.e1text.get())



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
