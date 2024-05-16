from pathlib import Path
from tkinter import messagebox
from tkinter import *
from math import sin, cos, tan, radians, log

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("500x430")
window.configure(bg = "#000000")
window.title("Calculator") 
window.iconbitmap("C:/Users/famil/Documents/Python/Assets/calc_icon.ico")

def num_click(num):
    now = field.get()
    field.delete(0, END)
    field.insert(0, str(now)+str(num))

def clr():
    field.delete(0, END)

def not_int():
    messagebox.showerror("Error", "Not an integer!")

def err_msg():
    messagebox.showerror("Error", "Invalid Input!")

def sqt():
    try:
        a = field.get()
        c = float(a) ** 0.5
        ans = "{:.3f}".format(c)
        field.delete(0, END)
        field.insert(0,ans)
    except ValueError:
        err_msg()

def eve():
    try:
        a = field.get()
        if float(a) == int(a):
            if int(a) % 2 == 0:
                field.delete(0,END)
                field.insert(0, str(a)+" is even")
            else:
                field.delete(0,END)
                field.insert(0, str(a)+" is odd")
        else:
            field.delete(0,END)
            not_int()
    except ValueError:
        not_int()

rad_sel = False
def toggle_rad():
    global rad_sel
    if rad_sel == True:
        rad_sel = False
        button_25 = Label(bg = "#212121",fg="#FFFFFF", font=("SF Pro Text", 14),anchor="center", text = "Degrees",relief="flat")
        button_25.place(x=0.0,y=360.0,width=100.0,height=40.0)
        button_26 = Button(bg = "#111111",fg="#FFFFFF", font=("SF Pro Text", 10),anchor="center",command=toggle_rad, text = "Switch to Rad.",relief="flat")
        button_26.place(x=0.0,y=400.0,width=100.0,height=30.0)
    else:
        rad_sel = True
        button_25 = Label(bg = "#212121",fg="#FFFFFF", font=("SF Pro Text", 14),anchor="center", text = "Radians",relief="flat")
        button_25.place(x=0.0,y=360.0,width=100.0,height=40.0)
        button_26 = Button(bg = "#111111",fg="#FFFFFF", font=("SF Pro Text", 10),anchor="center",command=toggle_rad, text = "Switch to Deg.",relief="flat")
        button_26.place(x=0.0,y=400.0,width=100.0,height=30.0)

def sin_calc():
    try:
        if rad_sel == True:
            a = float(field.get())
            field.delete(0, END)
            ans = sin(a)
            ans_string = "{:.6f}".format(ans)
            field.insert(0, ans_string)
        else:
            a = float(field.get())
            b = radians(a)
            field.delete(0, END)
            ans = sin(b)
            ans_string = "{:.6f}".format(ans)
            field.insert(0, ans_string)
    except ValueError:
        err_msg()

def cos_calc():
    try:
        if rad_sel == True:
            a = float(field.get())
            field.delete(0, END)
            ans = cos(a)
            ans_string = "{:.6f}".format(ans)
            field.insert(0, ans_string)
        else:
            a = float(field.get())
            b = radians(a)
            field.delete(0, END)
            ans = cos(b)
            ans_string = "{:.6f}".format(ans)
            field.insert(0, ans_string)
    except ValueError:
        err_msg()

def tan_calc():
    try:
        if rad_sel == True:
            a = float(field.get())
            field.delete(0, END)
            ans = tan(a)
            if ans >= 2000:
                field.insert(0, "Infinity")
            else:
                ans_string = "{:.6f}".format(ans)
                field.insert(0, ans_string)
        else:
            a = float(field.get())
            b = radians(a)
            field.delete(0, END)
            ans = tan(b)
            if ans >= 2000:
                field.insert(0, "Infinity")
            else:
                ans_string = "{:.6f}".format(ans)
                field.insert(0, ans_string)
    except ValueError:
        err_msg()

def ln():
    try:
        a = float(field.get())
        field.delete(0, END)
        if a >= 0:
            if a == 0:
                field.insert(0, "-Infinity")
            else:
                ans = log(a)
                ans_string = "{:.3f}".format(ans)
                field.insert(0, ans_string)
        else:
            messagebox.showerror("Error", "Enter a non negative number!")
    except ValueError:
        err_msg()
    
def token(input):
    try:
        a = float(field.get())
        global fnum, card
        fnum = a
        card = input
        field.delete(0, END)
    except ValueError:
        err_msg()
        
def calc():
    try:
        b = float(field.get())
        field.delete(0, END)
        if str(card) == "add":
            c = fnum + b
            field.insert(0, c)
        elif str(card) == "sub":
            c = fnum - b
            field.insert(0, c)
        elif str(card) == "mul":
            c = fnum*b
            field.insert(0,c)
        elif str(card) == "div":
            try:
                c = fnum/b 
                field.insert(0,c)
            except ZeroDivisionError:
                field.insert(0, "Undefined")
        elif str(card) == "pow":
            c = fnum**b
            field.insert(0,c)
    except ValueError:
        err_msg()
    except NameError:
        pass

canvas = Canvas(window,bg = "#000000",height = 360,width = 500,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(250.0,40.0,image=entry_image_1)

field = Entry(bd=0,bg="#5C5C5C",fg="#ffffff",highlightthickness=0,font=("SF Pro Text", 40))
field.place(x=0.0,y=0.0,width=500.0,height=78.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: num_click(7),relief="flat")
button_1.place(x=0.0,y=80.0,width=100.0,height=70.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: num_click(1),relief="flat")
button_2.place(x=0.0,y=220.0,width=100.0,height=70.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda: num_click(4),relief="flat")
button_3.place(x=0.0,y=150.0,width=100.0,height=70.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda: num_click(0),relief="flat")
button_4.place(x=0.0,y=290.0,width=100.0,height=70.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: num_click(8),relief="flat")
button_5.place(x=100.0,y=80.0,width=100.0,height=70.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: num_click(2),relief="flat")
button_6.place(x=100.0,y=220.0,width=100.0,height=70.0)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=lambda: num_click(5),relief="flat")
button_7.place(x=100.0,y=150.0,width=100.0,height=70.0)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_8 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=lambda: num_click("."),relief="flat")
button_8.place(x=100.0,y=290.0,width=100.0,height=70.0)

button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
button_9 = Button(image=button_image_9,borderwidth=0,highlightthickness=0,command=lambda: num_click(9),relief="flat")
button_9.place(x=200.0,y=80.0,width=100.0,height=70.0)

button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
button_10 = Button(image=button_image_10,borderwidth=0,highlightthickness=0,command=lambda: num_click(3),relief="flat")
button_10.place(x=200.0,y=220.0,width=100.0,height=70.0)

button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
button_11 = Button(image=button_image_11,borderwidth=0,highlightthickness=0,command=lambda: num_click(6),relief="flat")
button_11.place(x=200.0,y=150.0,width=100.0,height=70.0)

button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
button_12 = Button(image=button_image_12,borderwidth=0,highlightthickness=0,command=calc,relief="flat")
button_12.place(x=200.0, y=290.0, width=100.0, height=70.0)

button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))
button_13 = Button(image=button_image_13,borderwidth=0,highlightthickness=0,command=clr,relief="flat")
button_13.place(x=300.0,y=80.0,width=100.0,height=70.0)

button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
button_14 = Button(image=button_image_14,borderwidth=0,highlightthickness=0,command=lambda: token("sub"),relief="flat")
button_14.place(x=300.0,y=220.0,width=100.0,height=70.0)

button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))
button_15 = Button(image=button_image_15,borderwidth=0,highlightthickness=0,command=lambda: token("add"),relief="flat")
button_15.place(x=300.0, y=150.0,width=100.0,height=70.0)

button_image_16 = PhotoImage(file=relative_to_assets("button_16.png"))
button_16 = Button(image=button_image_16,borderwidth=0,highlightthickness=0,command=lambda:token("mul"),relief="flat")
button_16.place(x=300.0,y=290.0,width=100.0,height=70.0)

button_image_17 = PhotoImage(file=relative_to_assets("button_17.png"))
button_17 = Button(image=button_image_17,borderwidth=0,highlightthickness=0, command=lambda: token("div"), relief="flat")
button_17.place(x=400.0,y=80.0,width=100.0,height=70.0)

button_image_18 = PhotoImage(file=relative_to_assets("button_18.png"))
button_18 = Button(image=button_image_18,borderwidth=0,highlightthickness=0,command=sqt,relief="flat")
button_18.place(x=400.0, y=220.0,width=100.0,height=70.0)

button_image_19 = PhotoImage(file=relative_to_assets("button_19.png"))
button_19 = Button(image=button_image_19,borderwidth=0,highlightthickness=0,command=lambda: token("pow"),relief="flat")
button_19.place(x=400.0,y=150.0,width=100.0,height=70.0)

button_image_20 = PhotoImage(file=relative_to_assets("button_20.png"))
button_20 = Button(image=button_image_20,borderwidth=0,highlightthickness=0,command=eve,relief="flat")
button_20.place(x=400.0,y=290.0,width=100.0,height=70.0)

button_21 = Button(bg = "#111111",fg="#000000", font=("SF Pro Text", 18),anchor="center", text = "sin",command=sin_calc,relief="flat")
button_21.place(x=100.0,y=360.0,width=100.0,height=70.0)

button_22 = Button(bg = "#111111",fg="#000000", font=("SF Pro Text", 18),anchor="center", text = "cos",command=cos_calc,relief="flat")
button_22.place(x=200.0,y=360.0,width=100.0,height=70.0)

button_23 = Button(bg = "#111111",fg="#000000", font=("SF Pro Text", 18),anchor="center", text = "tan",command=tan_calc,relief="flat")
button_23.place(x=300.0,y=360.0,width=100.0,height=70.0)

button_24 = Button(bg = "#111111",fg="#000000", font=("SF Pro Text", 18),anchor="center", text = "ln",command=ln,relief="flat")
button_24.place(x=400.0,y=360.0,width=100.0,height=70.0)

button_25 = Label(bg = "#212121",fg="#FFFFFF", font=("SF Pro Text", 14),anchor="center", text = "Degrees",relief="flat")
button_25.place(x=0.0,y=360.0,width=100.0,height=40.0)

button_26 = Button(bg = "#111111",fg="#000000", font=("SF Pro Text", 10),anchor="center",command=toggle_rad, text = "Switch to Rad.",relief="flat")
button_26.place(x=0.0,y=400.0,width=100.0,height=30.0)

window.resizable(0, 0)
window.mainloop()