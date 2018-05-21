from tkinter import *

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

def enter_key(param):
    print(param)

def textbox():
    master = Tk()
    Label(master, text="Date").grid(row=0)
    Label(master, text="Item").grid(row=1)
    Label(master, text="Item Number").grid(row=2)
    Label(master, text="Where").grid(row=3)
    Label(master, text="Details").grid(row=4)
    Label(master, text="Price").grid(row=5)
    Label(master, text="Seller").grid(row=6)
    Label(master, text="Buyer").grid(row=7)
    Label(master, text="Initials").grid(row=8)
    Label(master, text="More Info").grid(row=9)

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master)
    e7 = Entry(master)
    e8 = Entry(master)
    e9 = Entry(master)
    e10 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)
    e9.grid(row=8, column=1)
    e10.grid(row=9, column=1)

    Button(master, text='Enter', command= lambda: enter_key("Code the command for entering data into database")).grid(row=10, column=1, sticky=W, pady=4)
    Button(master, text='Quit', command=master.quit).grid(row=10, column=0, sticky=W, pady=4)

    mainloop()

