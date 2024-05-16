from pathlib import Path
from tkinter import Tk, Canvas, Entry,Label, messagebox, Button, PhotoImage
from tkinter import *
import random

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Number Guess")
window.geometry("712x420")
window.configure(bg="#000000")

numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
x = int(random.choice(numList))
tries = 0
usedLetters = []

def reset():
    global x, tries, usedLetters,usedNum
    while usedNum == x:
        x = int(random.choice(numList))
    tries = 0
    usedLetters = []
    entry_1 = Label(bd=0,text="Enter a number:",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
    entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
    usedUpdate()

def win():
    global usedNum
    usedList = []
    usedList.append(x)
    usedNum = usedList.pop()
    tryList = []
    tryList.append(tries)
    tryes = tryList.pop()
    reset()
    root1 = Toplevel(window)
    root1.configure(bg="#000000")
    root1.title("Win!")
    Label(root1,text=" You Win!!! ",bg="#000000",fg="#00DF00", font=("SF Pro Text", 40 * -1), highlightthickness=0).pack()
    if tryes > 1:
        Label(root1,text=f"You guessed the word after {str(tryes)} guesses.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    elif tryes == 0:
        Label(root1,text="You got the word with no wrong guesses!!!",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    else:
        Label(root1,text="You guessed the word after 1 wrong guess.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    Label(root1,text=f"The number was {str(usedNum)}.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    root1.resizable(0,0)
    root1.mainloop()

def lose():
    global usedNum
    usedList = []
    usedList.append(x)
    usedNum = usedList.pop()
    reset()
    root1 = Toplevel(window)
    root1.configure(bg="#000000")
    root1.title("Lose!")
    Label(root1,text=" You Lost!!! ",bg="#000000",fg="#DF0000", font=("SF Pro Text", 40 * -1), highlightthickness=0).pack()
    Label(root1,text="You weren't able to guess the word within 7 guesses.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    Label(root1,text=f"The number was {str(usedNum)}.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    root1.resizable(0,0)
    root1.mainloop()

def usedUpdate():
    global tries
    if len(usedLetters) > 0:
        entry_2 = Label(bd=0,text="Your Guesses: "+", ".join(usedLetters),bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
        entry_2.place(x=0.0,y=310.0,width=712.0,height=58.0)
    else:
        entry_2 = Label(bd=0,text="Your Guesses: ",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
        entry_2.place(x=0.0,y=310.0,width=712.0,height=58.0)

    attempts = 7 - tries
    if attempts != 1:
        lbl = Label(bd=0,text=f"{str(attempts)} tries left.",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
        lbl.place(x=0.0,y=355.0,width=712.0,height=58.0)
    else:
        lbl = Label(bd=0,text=f"{str(attempts)} try left.",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
        lbl.place(x=0.0,y=355.0,width=712.0,height=58.0)

def go(event):
    global tries
    try:
        enteredValue = int(entry_3.get())
        if tries < 6:
            if enteredValue != x:
                if enteredValue < x:
                    entry_1 = Label(bd=0,text="Go a bit higher!",bg="#000000",fg="#78ACFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
                    entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
                    tries += 1
                    if str(enteredValue) not in usedLetters:
                        usedLetters.append(str(enteredValue))
                    usedUpdate()
                    entry_3.delete(0, END)
                else:
                    entry_1 = Label(bd=0,text="Go a bit lower!",bg="#000000",fg="#78FFAC", font=("SF Pro Text", 40 * -1), highlightthickness=0)
                    entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
                    tries += 1
                    if str(enteredValue) not in usedLetters:
                        usedLetters.append(str(enteredValue))
                    usedUpdate()
                    entry_3.delete(0, END)
            else:
                entry_3.delete(0, END)
                win()
        else:
            entry_3.delete(0, END)
            if enteredValue != x:
                usedUpdate()
                lose()
            else:
                win()
    except ValueError:
        entry_3.delete(0, END)
        messagebox.showerror("Error", "Enter a valid number!")

canvas = Canvas(window,bg = "#000000",height = 400,width = 712,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(356.0,142.99999999999997,image=entry_image_1)
entry_1 = Label(bd=0,text="Enter a number:",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(356.0,362.0,image=entry_image_2)
entry_2 = Label(bd=0,text="Your Guesses: ",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
entry_2.place(x=0.0,y=310.0,width=712.0,height=58.0)

canvas.create_text(270.0,0,anchor="nw",text="Guess It!",fill="#FFFFFF",font=("Sitka Heading Bold", 40 * -1))
canvas.create_text(175.0,69.99999999999997,anchor="nw",text="Guess the number between 1 and 100 within 7 tries.",fill="#FFFFFF",font=("SF Pro Text", 15 * -1))

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(356.0,229.99999999999997,image=entry_image_3)
entry_3 = Entry(bd=0,bg="#353535",fg="#FFFFFF", font=("SF Pro Text", 38 * -1),highlightthickness=0)
entry_3.place(x=331.0,y=199.99999999999997,width=50.0,height=58.0,)

lbl = Label(bd=0,text="7 tries left.",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
lbl.place(x=0.0,y=355.0,width=712.0,height=58.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,relief="flat",command=lambda:go('none'))
button_1.place(x=326.0,y=275.0,width=60.0,height=30.0)

entry_3.bind('<KeyPress-Return>', go)

window.resizable(0, 0)
window.mainloop()