from pathlib import Path
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage, Toplevel, messagebox
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("800x350")
window.configure(bg = "#000000")
window.title("Bill Generator")

canvas = Canvas(window,bg = "#000000",height = 350,width = 800,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_text(283.0,52.0,anchor="nw",text="BILL GENERATOR",fill="#FFFFFF",font=("SF Pro Text", 24 * -1))
canvas.create_text(260.0,5.0,anchor="nw",text="General Store",fill="#FFFFFF",font=("SF Pro Text", 40 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(199.5,173.0,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#8C8C8C",fg="#FFFFFF",font=("SF Pro Text", 20 * -1),highlightthickness=0)
entry_1.place(x=116.0,y=155.0,width=167.0,height=34.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(199.5,237.0,image=entry_image_2)
entry_2 = Label(bd=0,bg="#595959",highlightthickness=0)
entry_2.place(x=116.0,y=219.0,width=167.0,height=34.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(483.5,237.0,image=entry_image_3)
entry_3 = Label(bd=0,bg="#595959",highlightthickness=0)
entry_3.place(x=400.0,y=219.0,width=167.0,height=34.0)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(483.0,170.0,image=entry_image_4)
entry_4 = Entry(bd=0,bg="#8C8C8C",fg="#FFFFFF",font=("SF Pro Text", 20 * -1),highlightthickness=0)
entry_4.place(x=399.5,y=152.0,width=167.0,height=34.0)

canvas.create_text(33.0,157.0,anchor="nw",text="Item ID:",fill="#FFFFFF",font=("SF Pro Text", 22 * -1))
canvas.create_text(302.0,157.0,anchor="nw",text="Quantity:",fill="#FFFFFF",font=("SF Pro Text", 22 * -1))

bill_items = []
global total
total = 0

class items:
    def __init__(self, name, id, price, added):
        self.name = name
        self.id = id
        self.price = price
        self.added = added

Milk = items("Milk", "001", 15, False)
Biscuits = items("Biscuits", "002", 25, False)
Chips = items("Chips", "003", 15, False)
Coke = items("Coca-Cola", "004", 45, False)
Butter = items("Butter", "005", 60, False)
Soap = items("Toilet Soap", "006", 65, False)
Shampoo = items("Shampoo", "007", 215, False)
Washing = items("Washing Powder", "008", 75, False)
Oil = items("Cooking Oil", "009", 145, False)
Ketchup = items("Ketchup", "010", 120, False)
Tea = items("Tea Leaves", "011", 180, False)
Toothpaste = items("Toothpaste", "012", 135, False)
Noodles = items("Noodles", "013", 75, False)
Ball = items("Ball", "014", 30, False)
Chocolate = items("Chocolate", "015", 20, False)
Yoghurt = items("Yoghurt", "016", 30, False)
Eggs = items("Eggs", "017", 60, False)
Bottle = items("Bottle", "018", 1000, False)

inventory = [Milk,Biscuits, Chips, Coke, Butter, Soap, Washing, Shampoo, Oil, Ketchup, Tea, Toothpaste, Noodles, Ball, Chocolate, Yoghurt, Eggs,Bottle]
no_of_items = len(inventory)

def clear():
    global total
    total = 0
    bill_items.clear()
    entry_3 = Label(bd=0,bg="#595959",text="", fg="#FFFFFF",font=("SF Pro Text", 22 * -1),highlightthickness=0)
    entry_3.place(x=400.0,y=219.0,width=167.0,height=34.0)
    entry_2 = Label(bd=0,bg="#595959",text="",fg="#FFFFFF",font=("SF Pro Text", 22 * -1),highlightthickness=0)
    entry_2.place(x=116.0,y=219.0,width=167.0,height=34.0)
    entry_1.delete(0, END)
    entry_4.delete(0, END)

def disp_total():
    entry_3 = Label(bd=0,bg="#595959",text="Rs. "+str(total), fg="#FFFFFF",font=("SF Pro Text", 22 * -1),highlightthickness=0).place(x=400.0,y=219.0,width=167.0,height=34.0)

def id_err():
    entry_1.delete(0, END)
    messagebox.showerror("Error", "Please enter a valid ID from the Menu")

def inv_inp():
    entry_1.delete(0, END)
    entry_4.delete(0, END)
    messagebox.showerror("Error", "Invalid Input!")
    
def add():
    global total
    try:
        x = int(entry_1.get())
        quantity = int(entry_4.get())
        if x <= no_of_items:
            for thing in inventory:
                if int(thing.id) == x:
                    for x in range(0, quantity):
                        bill_items.append(str(thing.name))
                        total = total + int(thing.price)
                        disp_total()
                    entry_2 = Label(bd=0,bg="#595959",text="Rs. " + str(thing.price) + " each",fg="#FFFFFF",font=("SF Pro Text", 22 * -1),highlightthickness=0).place(x=116.0,y=219.0,width=167.0,height=34.0)
        else:
            id_err()
    except ValueError:
        inv_inp()   

def remove():
    global total
    if len(bill_items) > 0:
        x = bill_items.pop()
        for thing in inventory:
            if str(x) == str(thing.name):
                total = total - int(thing.price)
                disp_total()
        try:
            for bong in inventory:
                if str(bill_items[-1]) == bong.name:
                    entry_2 = Label(bd=0,bg="#595959",text="Rs. " + str(bong.price) + " each",fg="#FFFFFF",font=("SF Pro Text", 22 * -1),highlightthickness=0).place(x=116.0,y=219.0,width=167.0,height=34.0)
        except IndexError:
            pass

def generate():
    if total != 0:
        bill = Toplevel(window)
        bill.title("Bill")
        bill.resizable(0, 0)
        bill.configure(bg="#000000")
        Label(bill, text="TRANSACTION RECEIPT",font=("SF Pro Text", 24 * -1),bg="#000000",fg="#FFFFFF").pack()
        Label(bill, text="--------------------------------",font=("SF Pro Text", 22 * -1),bg="#000000",fg="#FFFFFF").pack()
        for item in bill_items:
            for thing in inventory:
                if str(item) == thing.name:
                    if thing.added == False:
                        Label(bill, text=str(thing.name)+ "  -   " + str(bill_items.count(thing.name)) + " units",font=("SF Pro Text", 22 * -1),bg="#000000",fg="#FFFFFF").pack()
                        thing.added = True
        Label(bill, text="--------------------------------",font=("SF Pro Text", 22 * -1),bg="#000000",fg="#FFFFFF").pack()
        Label(bill, text="Your Total is: Rs. " + str(total) + ".00",font=("SF Pro Text", 22 * -1),bg="#000000",fg="#FFFFFF").pack()
        clear()
    else:
        pass

def menu():
    menu = Toplevel(window)
    menu.title("Inventory")
    menu.resizable(0, 0)
    menu.configure(bg="#000000")
    Label(menu, text="ITEM LIST",font=("SF Pro Text", 28 * -1),bg="#000000",fg="#FFFFFF").pack()
    Label(menu, text="-----------------------------------------------",font=("SF Pro Text", 22 * -1),bg="#000000",fg="#FFFFFF").pack()
    for thing in inventory:
        Label(menu, text=str(thing.id) + "   -   " + str(thing.name) + "   -   Rs. " + str(thing.price) + " each",font=("SF Pro Text", 22 * -1),bg="#000000",fg="#FFFFFF").pack()
    Label(menu, text="-----------------------------------------------",font=("SF Pro Text", 22 * -1),bg="#000000",fg="#FFFFFF").pack()

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=menu,relief="flat").place(x=47.0,y=60.0,width=100.0,height=30.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=add,relief="flat").place(x=648.0,y=142.0,width=116.0,height=46.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=remove,relief="flat").place(x=648.0,y=209.0,width=116.0,height=46.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=clear,relief="flat").place(x=200.0,y=292.0,width=116.0,height=46.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=generate,relief="flat").place(x=342.0,y=290.0,width=127.0,height=46.0)

canvas.create_text(47.0,225.0,anchor="nw",text="Price:",fill="#FFFFFF",font=("SF Pro Text", 22 * -1))
canvas.create_text(330.0,225.0,anchor="nw",text="Total:",fill="#FFFFFF",font=("SF Pro Text", 22 * -1))

window.resizable(0, 0)
window.mainloop()