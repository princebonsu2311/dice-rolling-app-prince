from PIL import ImageTk, Image
import tkinter as tk
import random

from typing import List

window = tk.Tk()

window.title("Dice roll game")
window.geometry("1200x1200")

back_img = tk.PhotoImage("newbackground@3x.png")
background_label = tk.Label(window, image=back_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image_names = back_img



def roll(y):
    list_of_objects = ['d1' , 'd2', 'd3', 'd4', 'd5', 'd6']
    randomize1 = random.choice(list_of_objects)
    randomize2 = random.choice(list_of_objects)
    print(randomize1, randomize2)
    if randomize1 == 'di':
        answer.config(image=roll1)

    elif randomize1 == 'd1':
        answer.config(image=roll1)

    elif randomize1 == 'd1':
        answer.config(image=roll2)

    elif randomize1 == 'd1':
        answer.config(image=roll3)

    elif randomize1 == 'd1':
        answer.config(image=roll4)

    elif randomize1 == 'd1':
        answer.config(image=roll5)

    elif randomize1 == 'd1':
        answer.config(image=roll6)

    if randomize2 == 'd1':
        answer.config(image=roll1)

    elif randomize2== 'd1':
        answer.config(image=roll2)

    elif randomize2== 'd1':
        answer.config(image=roll3)

    elif randomize2== 'd1':
        answer.config(image=roll4)

    elif randomize2== 'd1':
        answer.config(image=roll5)

    elif randomize12== 'd1':
        answer.config(image=roll6)


number = random.randint(1,6)


roll1 = tk.PhotoImage(file="dice1@3x.png")

roll2 = tk.PhotoImage(file="dice2@3x.png")

roll3 = tk.PhotoImage(file="dice3@3x.png")

roll4 = tk.PhotoImage(file="dice4@3x.png")

roll5 = tk.PhotoImage(file="dice5@3x.png")

roll6 = tk.PhotoImage(file="dice6@3x.png")

# Button

button_photo = ImageTk.PhotoImage(file="Icon-60@3x.png")

button = tk.Button(width="150", height="150", image=button_photo)

button.bind("<button-1>", roll)

button.pack(side=" top", pady=50)

answer = tk.label(image="dice1")







answer2 = tk.label(image="dice1")

answer.pack()

answer.place(x=100, y=400)

answer2.pack()

answer3 = tk.label(x=600, y=400)
print(number)

window.mainlop()

