from pathlib import Path
from tkinter import Tk, Canvas, Entry,Label, messagebox, Button, PhotoImage
from tkinter import *
import random

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Word Guess")
window.geometry("712x420")
window.configure(bg = "#000000")

canvas = Canvas(window,bg = "#000000",height = 400,width = 712,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

class word():
    def __init__(self, name, rep, rep_ind, rep_let):
        self.name = name
        self.rep = rep
        self.rep_ind = rep_ind
        self.rep_let = rep_let

w1 = word("Abort", False, 0, "")
w2 = word("Pulse", False, 0, "")
w3 = word("Badge", False, 0, "")
w4 = word("Larva", True, 4, "a")
w5 = word("Ivory", False, 0, "")
w6 = word("Major", False, 0, "")
w7 = word("Ultra", False, 0, "")
w8 = word("Youth", False, 0, "")
w9 = word("Spray", False, 0, "")
w10 = word("Sever", True, 3, "e")
w11 = word("Serve", True, 4, "e")
w12 = word("Trash", False, 0, "")
w13 = word("Rogue", False, 0, "")
w14 = word("Query", False, 0, "")
w15 = word("Heist", False, 0, "")
w16 = word("Labor", False, 0, "")
w17 = word("Floss", True, 4, "s")
w18 = word("Death", False, 0, "")
w19 = word("Focus", False, 0, "")
w20 = word("Choke", False, 0, "")
w21 = word("Voice", False, 0, "")
w22 = word("Tryst", True, 4, "t")
w23 = word("Havoc", False, 0, "")
w24 = word("Wrong", False, 0, "")
w25 = word("Green", True, 3, "e")
w26 = word("Blind", False, 0, "")
w27 = word("Sword", False, 0, "")
w28 = word("Crime", False, 0, "")
w29 = word("Slice", False, 0, "")
w30 = word("Digit", True, 3, "i")
w41 = word("Wrath", False, 0, "")
w42 = word("Grave", False, 0, "")
w43 = word("Sober", False, 0, "")
w44 = word("Chime", False, 0, "")
w45 = word("Sleep", True, 3, "e")
w46 = word("Drunk", False, 0, "")
w47 = word("Jenga", False, 0, "")
w48 = word("Prune", False, 0, "")
w49 = word("Soggy", True, 3, "g")
w50 = word("Stunt", True, 4, "t")
w31 = word("Zebra", False, 0 , "")
w32 = word("Brine", False, 0 , "")
w33 = word("Choir", False, 0 , "")
w34 = word("Genre", True, 4 , "e")
w35 = word("Shaft", False, 0 , "")
w36 = word("Naive", False, 0 , "")
w37 = word("Stump", False, 0 , "")
w38 = word("Ahead", True, 3 , "a")
w39 = word("Opine", False, 0 , "")
w40 = word("Polar", False, 0 , "")
w51 = word("Allot", True, 2, "l")
w52 = word("Ranch", False, 0, "")
w53 = word("Clock", True, 3, "c")
w54 = word("Annex", True, 2, "n")
w55 = word("Pixel", False, 0, "")
w56 = word("Exact", False, 0, "")
w57 = word("Shine", False, 0, "")

word_list = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,w28,w29,w30,w31,w32,w33,w34,w35,w36,w37,w38,w39,w40,w41,w42,w43,w44,w45,w46,w47,w48,w49,w50,w51,w52,w53,w54,w55,w56,w57]
chosen = random.choice(word_list)
container = []
used_letters = []
player_word = ["__", "__", "__", "__", "__"]
fails = 0
list = []
list2 = []

for letter in chosen.name:
    container.append(letter)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(356.0,142.99999999999997,image=entry_image_1)
entry_1 = Label(bd=0,text="  ".join(player_word),bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(356.0,362.0,image=entry_image_2)
entry_2 = Label(bd=0,text="Used Letters: ",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
entry_2.place(x=0.0,y=310.0,width=712.0,height=58.0)

canvas.create_text(270.0,0,anchor="nw",text="Guess It!",fill="#FFFFFF",font=("Sitka Heading Bold", 40 * -1))
canvas.create_text(158.0,69.99999999999997,anchor="nw",text="Get to the five lettered word within 10 wrong guesses.",fill="#FFFFFF",font=("SF Pro Text", 15 * -1))

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(356.0,229.99999999999997,image=entry_image_3)
entry_3 = Entry(bd=0,bg="#353535",fg="#FFFFFF", font=("SF Pro Text", 40 * -1),highlightthickness=0)
entry_3.place(x=331.0,y=199.99999999999997,width=50.0,height=58.0,)

lbl = Label(bd=0,text="10 tries left.",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
lbl.place(x=0.0,y=355.0,width=712.0,height=58.0)

def reset():
    entry_1 = Label(bd=0,text="__  __  __  __  __",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
    entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
    entry_2 = Label(bd=0,text="Used Letters: ",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
    entry_2.place(x=0.0,y=310.0,width=712.0,height=58.0)
    lbl = Label(bd=0,text="10 tries left.",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
    lbl.place(x=0.0,y=355.0,width=712.0,height=58.0)

def used_update():
    if len(used_letters) > 0:
        entry_2 = Label(bd=0,text="Used Letters: "+", ".join(used_letters),bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
        entry_2.place(x=0.0,y=310.0,width=712.0,height=58.0)

    tries = 10 - fails
    if tries != 1:
        lbl = Label(bd=0,text=str(tries)+" tries left.",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
        lbl.place(x=0.0,y=355.0,width=712.0,height=58.0)
    else:
        lbl = Label(bd=0,text=str(tries)+" try left.",bg="#000000", fg="#FFFFFF", font=("SF Pro Text", 25 * -1),highlightthickness=0)
        lbl.place(x=0.0,y=355.0,width=712.0,height=58.0)


def win():
    global list, list2
    root1 = Toplevel(window)
    root1.configure(bg="#000000")
    root1.title("Win!")
    Label(root1,text=" You Win!!! ",bg="#000000",fg="#00DF00", font=("SF Pro Text", 40 * -1), highlightthickness=0).pack()
    if len(list) > 1:
        Label(root1,text="You guessed the word after "+str(len(list))+" wrong guesses.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    elif len(list) == 0:
        Label(root1,text="You got the word with no wrong guesses!!!",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    else:
        Label(root1,text="You guessed the word after "+str(len(list))+" wrong guess.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    Label(root1,text="The word was " + str("".join(list2)).upper()+".",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    list = []
    list2 = []
    root1.resizable(0,0)
    root1.mainloop()

def lose():
    global list2
    root1 = Toplevel(window)
    root1.configure(bg="#000000")
    root1.title("Lose!")
    Label(root1,text=" You Lost!!! ",bg="#000000",fg="#DF0000", font=("SF Pro Text", 40 * -1), highlightthickness=0).pack()
    Label(root1,text="You weren't able to guess the word in 10 wrong guesses.",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    Label(root1,text="The word was " + str("".join(list2)).upper()+".",bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 20 * -1), highlightthickness=0).pack()
    list2 = []
    root1.resizable(0,0)
    root1.mainloop()

def check_win():
    global list, list2, fails, container, player_word, used_letters, chosen, letter
    old_word = "".join(container)
    if str(''.join(player_word).lower()) == str(''.join(container).lower()):
        list = used_letters.copy()
        list2 = container.copy()
        reset()
        while True:
                chosen = random.choice(word_list)
                if old_word.lower() != str(chosen.name).lower():
                    break
        container = []
        used_letters = []
        player_word = ["__", "__", "__", "__", "__"]
        fails = 0
        for letter in chosen.name:
            container.append(letter)
        win()

def check_lose():
    global list, list2, fails, container, player_word, used_letters, chosen, letter
    old_word = "".join(container)
    if fails == 10:
        if str(''.join(player_word).lower()) != str(''.join(container).lower()):
            list2 = container.copy()
            reset()
            while True:
                chosen = random.choice(word_list)
                if old_word.lower() != str(chosen.name).lower():
                    break
            container = []
            used_letters = []
            player_word = ["__", "__", "__", "__", "__"]
            fails = 0
            for letter in chosen.name:
                container.append(letter)
            lose()

def go(event):
    global list, list2, fails, container, player_word, used_letters, chosen, letter
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if chosen.rep == False:
        x = entry_3.get()
        entry_3.delete(0, END)
        exec = False
        if len(str(x)) == 1 and x.lower() in alphabet:
            for letter in container:
                ind = container.index(letter)
                if fails <= 9:
                    if str(x.lower()) == str(letter.lower()):
                        player_word.insert(ind, x.upper())
                        player_word.pop(ind+1)
                        entry_1 = Label(bd=0,text="  ".join(player_word),bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
                        entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
                        exec = True
            if exec == False:
                fails += 1
                entry_1 = Label(bd=0,text="  ".join(player_word),bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
                entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
                if x.upper() not in used_letters: 
                    used_letters.append(x.upper())
                used_update()
            check_win()
            check_lose()
        else:
            messagebox.showerror("Error", "Enter a single alphabet.")
    else:
        x = entry_3.get()
        entry_3.delete(0, END)
        exec = False
        if len(str(x)) == 1 and x.lower() in alphabet:
            if x.lower() != str(chosen.rep_let).lower():
                for letter in container:
                    ind = container.index(letter)
                    if fails <= 9:
                        if str(x.lower()) == str(letter.lower()):
                            player_word.insert(ind, x.upper())
                            player_word.pop(ind+1)
                            entry_1 = Label(bd=0,text="  ".join(player_word),bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
                            entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
                            exec = True
            else:
                for letter in container:
                    if fails <= 9:
                            ind = container.index(letter)
                            if str(x.lower()) == str(letter.lower()):
                                player_word.insert(ind, x.upper())
                                player_word.pop(ind+1)
                                player_word.insert(chosen.rep_ind, x.upper())
                                player_word.pop(chosen.rep_ind+1)
                                entry_1 = Label(bd=0,text="  ".join(player_word),bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
                                entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
                                exec = True
            if exec == False:
                fails += 1
                entry_1 = Label(bd=0,text="  ".join(player_word),bg="#000000",fg="#FFFFFF", font=("SF Pro Text", 40 * -1), highlightthickness=0)
                entry_1.place(x=160.0,y=112.99999999999997,width=392.0,height=58.0)
                if x.upper() not in used_letters: 
                    used_letters.append(x.upper())
                used_update()
            check_win()
            check_lose()
        else:
            messagebox.showerror("Error", "Enter a single alphabet.")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda:go('none'),relief="flat")
button_1.place(x=326.0,y=275.0,width=60.0,height=30.0)

entry_3.bind('<KeyPress-Return>', go)

window.resizable(0, 0)
window.mainloop()