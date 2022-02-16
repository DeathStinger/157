from tkinter import *
from PIL import ImageTk,Image
import random

root=Tk()
root.title("Pokemon Game")
root.geometry("600x400")
root.configure(background="blue")
img= ImageTk.PhotoImage(Image.open("il_794xN.2205501544_i59b.jpg"))
img1= ImageTk.PhotoImage(Image.open("11.jpg"))

player1=Label(root,text="Player 1",bg="royal blue",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="Player 2",bg="royal blue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_scorelabel1=Label(root,bg="royal blue",fg="white")
player1_scorelabel1.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_scorelabel1=Label(root,bg="royal blue",fg="white")
player2_scorelabel1.place(relx=0.9,rely=0.4,anchor=CENTER)

random_dice_label=Label(root,bg="chocolate1",fg="white")
random_dice_label.place(relx=0.5,rely=0.5,anchor=CENTER)

player1_score=0
def player1():
    global player1_score
    random_no = random.randint(1,6)
    random_dice_label["text"]= "Player1 Dice Random Number : "+ str(random_no)
    player1_score=player1_score+random_no
    player1_scorelabel1["text"]=str(player1_score)
    
btn1=Button(root,image=img,command=player1)
btn1.place(relx=0.1,rely=0.6,anchor=CENTER)

player2_score=0
def player2():
    global player2_score
    random_no1=random.randint(1,6)
    random_dice_label["text"]="PLayer2 Dice Random Number : "+str(random_no1)
    player2_score=player2_score+random_no1
    player2_scorelabel1["text"]=str(player2_score)
    
btn2=Button(root,image=img1,command=player2)
btn2.place(relx=0.9,rely=0.6,anchor=CENTER)
    

root.mainloop()


