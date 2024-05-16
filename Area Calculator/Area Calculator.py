from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1015x715")
window.configure(bg = "#000000")
window.title("Area Calculator")

canvas = Canvas(window,bg = "#000000",height = 715,width = 1015,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(255.0,199.99999999999994,image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(758.0,404.99999999999994,image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(255.0,404.99999999999994,image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(506.0,610.0,image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(758.0,199.99999999999994,image=image_image_5)

canvas.create_text(320.0,20.999999999999943,anchor="nw",text="Area Calculator",fill="#FFFFFF",font=("SF Pro Text", 48 * -1))
canvas.create_text(70.0,116.99999999999994,anchor="nw",text="Circle",fill="#FFFFFF",font=("SF Pro Text", 24 * -1))
canvas.create_text(62.0,321.99999999999994,anchor="nw",text="Square",fill="#FFFFFF",font=("SF Pro Text", 24 * -1))
canvas.create_text(569.0,116.99999999999994,anchor="nw",text="Ellipse",fill="#FFFFFF",font=("SF Pro Text", 24 * -1))
canvas.create_text(549.0,322.0,anchor="nw",text="Rectangle",fill="#FFFFFF",font=("SF Pro Text", 24 * -1))
canvas.create_text(60.0,529.0,anchor="nw",text="Triangle",fill="#FFFFFF",font=("SF Pro Text", 24 * -1))

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(104.0,211.99999999999994,image=image_image_6)

canvas.create_text(213.0,117.99999999999994,anchor="nw",text="Enter the radius(in cm):",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(213.0,322.99999999999994,anchor="nw",text="Enter the side(in cm):",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(716.0,117.99999999999994,anchor="nw",text="Semi-Axis 1(in cm):",fill="#FFFFFF",font=("SF Pro Text", 14 * -1))
canvas.create_text(716.0,322.99999999999994,anchor="nw",text="Length(in cm):",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(197.0,529.0,anchor="nw",text="Base length(in cm):",fill="#FFFFFF",font=("SF Pro Text", 14 * -1))
canvas.create_text(539.0,530.0,anchor="nw",text="Side 1(in cm):",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(703.0,530.0,anchor="nw",text="Side 2(in cm):",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(867.0,530.0,anchor="nw",text="Side 3(in cm):",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(863.0,117.99999999999994,anchor="nw",text="Semi-Axis 2(in cm):",fill="#FFFFFF",font=("SF Pro Text", 14 * -1))
canvas.create_text(863.0,322.99999999999994,anchor="nw",text="Breadth(in cm):",fill="#FFFFFF",font=("SF Pro Text", 14 * -1))
canvas.create_text(344.0,529.0,anchor="nw",text="Height(in cm):",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(213.0,211.99999999999994,anchor="nw",text="Area:",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(213.0,416.99999999999994,anchor="nw",text="Area:",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(716.0,211.99999999999994,anchor="nw",text="Area:",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(716.0,416.99999999999994,anchor="nw",text="Area:",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(197.0,623.0,anchor="nw",text="Area:",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))
canvas.create_text(539.0,623.0,anchor="nw",text="Area:",fill="#FFFFFF",font=("SF Pro Text", 16 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(344.5,156.49999999999994,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_1.place(x=229.5,y=139.99999999999994,width=230.0,height=31.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(344.5,361.49999999999994,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_2.place(x=229.5,y=344.99999999999994,width=230.0,height=31.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(774.0,156.49999999999994,image=entry_image_3)
entry_3 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_3.place(x=732.5,y=139.99999999999994,width=83.0,height=31.0)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(774.0,361.49999999999994,image=entry_image_4)
entry_4 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_4.place(x=732.5,y=344.99999999999994,width=83.0,height=31.0)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(255.0,567.5,image=entry_image_5)
entry_5 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_5.place(x=213.5,y=551.0,width=83.0,height=31.0)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(597.0,568.5,image=entry_image_6)
entry_6 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_6.place(x=555.5,y=552.0,width=83.0,height=31.0)

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(761.0,568.5,image=entry_image_7)
entry_7 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_7.place(x=719.5,y=552.0,width=83.0,height=31.0)

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(925.0,568.5,image=entry_image_8)
entry_8 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_8.place(x=883.5,y=552.0,width=83.0,height=31.0)

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(921.0,156.49999999999994,image=entry_image_9)
entry_9 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_9.place(x=879.5,y=139.99999999999994,width=83.0,height=31.0)

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(921.0,361.49999999999994,image=entry_image_10)
entry_10 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_10.place(x=879.5,y=344.99999999999994,width=83.0,height=31.0)

entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(402.0,567.5,image=entry_image_11)
entry_11 = Entry(bd=0,bg="#5C5C5C",fg="#FFFFFF",font=("SF Pro Text", 16 * -1),highlightthickness=0)
entry_11.place(x=360.5,y=551.0,width=83.0,height=31.0)

entry_image_12 = PhotoImage(file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(344.5,250.49999999999994,image=entry_image_12)
entry_12 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",highlightthickness=0)
entry_12.place(x=229.5,y=233.99999999999994,width=230.0,height=31.0)

entry_image_13 = PhotoImage(file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(344.5,455.49999999999994,image=entry_image_13)
entry_13 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",highlightthickness=0)
entry_13.place(x=229.5,y=438.99999999999994,width=230.0,height=31.0)

entry_image_14 = PhotoImage(file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(847.5,250.49999999999994,image=entry_image_14)
entry_14 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",highlightthickness=0)
entry_14.place(x=732.5,y=233.99999999999994,width=230.0,height=31.0)

entry_image_15 = PhotoImage(file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(847.5,455.49999999999994,image=entry_image_15)
entry_15 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text="",highlightthickness=0)
entry_15.place(x=732.5,y=438.99999999999994,width=230.0,height=31.0)

entry_image_16 = PhotoImage(file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(328.5,661.5,image=entry_image_16)
entry_16 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",highlightthickness=0)
entry_16.place(x=213.5,y=645.0,width=230.0,height=31.0)

entry_image_17 = PhotoImage(file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(761.0,661.5,image=entry_image_17)
entry_17 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",highlightthickness=0)
entry_17.place(x=555.5,y=645.0,width=411.0,height=31.0)

def err_msg():
    messagebox.showerror("Error", "Invalid Input!")

def circle():
    try:
        r = float(entry_1.get())
        pi = 3.141
        if r >= 0:
            ar = pi*r*r
            x = '%.2f' % ar
            entry_12 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = str(x) + " sq. cm",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_12.place(x=229.5,y=233.99999999999994,width=230.0,height=31.0)
        else:
            entry_12 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = "Undefined",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_12.place(x=229.5,y=233.99999999999994,width=230.0,height=31.0)
    except ValueError:
        err_msg()

def sqr():
    try:
        r = float(entry_2.get())
        if r >= 0:
            ar = r*r
            x = '%.1f' % ar
            entry_13 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = str(x) + " sq. cm",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_13.place(x=229.5,y=438.99999999999994,width=230.0,height=31.0)
        else:
            entry_13 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = "Undefined",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_13.place(x=229.5,y=438.99999999999994,width=230.0,height=31.0)
    except ValueError:
        err_msg()

def ell():
    try:
        a = float(entry_3.get())
        b = float(entry_9.get())
        if a >= 0 and b >= 0:
            pi = 3.141
            ar = pi*a*b
            x = '%.2f' % ar
            entry_14 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = str(x) + " sq. cm",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_14.place(x=732.5,y=233.99999999999994,width=230.0,height=31.0)
        else:
            entry_14 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = "Undefined",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_14.place(x=732.5,y=233.99999999999994,width=230.0,height=31.0)
    except ValueError:
        err_msg()
    
def rect():
    try:
        a = float(entry_4.get())
        b = float(entry_10.get())
        if a >= 0 and b >= 0:
            ar = a*b
            x = '%.1f' % ar
            entry_15 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = str(x) + " sq. cm",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_15.place(x=732.5,y=438.99999999999994,width=230.0,height=31.0)
        else:
            entry_15 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = "Undefined",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_15.place(x=732.5,y=438.99999999999994,width=230.0,height=31.0)
    except ValueError:
        err_msg()

def tri1():
    try:
        a = float(entry_5.get())
        b = float(entry_11.get())
        if a >= 0 and b >=0:
            ar = 0.5*a*b
            x = '%.1f' % ar
            entry_16 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = str(x) + " sq. cm",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_16.place(x=213.5,y=645.0,width=230.0,height=31.0)
        else:
            entry_16 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = "Undefined",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_16.place(x=213.5,y=645.0,width=230.0,height=31.0)
    except ValueError:
        err_msg()

def tri2():
    try:
        a = float(entry_6.get())
        b = float(entry_7.get())
        c = float(entry_8.get())
        if a >= 0 and b >= 0 and c >= 0:
            s = (a+b+c)/2
            d = s-a
            e = s-b
            f = s-c
            area_sq = s*d*e*f
            ar = (area_sq)**0.5
            x = '%.1f' %ar
            entry_17 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = str(x) + " sq. cm",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_17.place(x=555.5,y=645.0,width=411.0,height=31.0)
        else:
            entry_17 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = "Undefined",highlightthickness=0,font=("SF Pro Text", 16 * -1))
            entry_17.place(x=555.5,y=645.0,width=411.0,height=31.0)
    except ValueError:
        err_msg()
    except TypeError:
        entry_17 = Label(bd=0,bg="#5C5C5C",fg="#FFFFFF",text = "Undefined",highlightthickness=0,font=("SF Pro Text", 16 * -1))
        entry_17.place(x=555.5,y=645.0,width=411.0,height=31.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=sqr,relief="flat")
button_1.place(x=304.0,y=387.99999999999994,width=82.0,height=33.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=circle,relief="flat")
button_2.place(x=304.0,y=182.99999999999994,width=82.0,height=33.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=ell,relief="flat")
button_3.place(x=798.0,y=180.99999999999994,width=82.0,height=33.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=rect,relief="flat")
button_4.place(x=798.0,y=387.99999999999994,width=82.0,height=33.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=tri2,relief="flat")
button_5.place(x=733.0,y=593.0,width=82.0,height=33.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=tri1,relief="flat")
button_6.place(x=304.0,y=594.0,width=82.0,height=33.0)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(104.0,416.99999999999994,image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(605.0,416.99999999999994,image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(607.0,211.99999999999994,image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(507.0,609.0,image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(104.0,627.0,image=image_image_11)

window.resizable(0, 0)
window.mainloop()