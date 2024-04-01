
import random as rm
import time
import tkinter as tk
from tkinter import simpledialog

name = ''

def quit():
    app.quit()
def get_name():
    name = simpledialog.askstring("Greetings player", "Enter your name:")
    if name:
        label.config(text= name + "!...., Sounds like a wonderful name")
    btn.config(text = 'next', command=next)

def start():

    obj = rm.Random(time.time())
    random_fruit = obj.choice(fruits)
    n = len(random_fruit)

    letters = ['_ ' for letter in random_fruit]
    answer = [letter for letter in random_fruit]
    disp = len(random_fruit)*'_ '
    label.config(text=disp)
    count = 6
    txt = 'Your guess'
    while count > 0:
        guess = simpledialog.askstring(txt,'->')
        if guess in answer:
            txt = 'Correct, next guess?'
            pos = answer.index(guess)
            answer[pos] = '*'
            letters[pos] = guess
            n-= 1
            if n ==0:
                txt = "Congratulations!, you have won!"
                label.config(text = txt)
                break
        else:
            count -= 1
            if count != 0:
               txt = f"Incorrect, you have {count} chances left"
               label.config(text =txt)
               draw_hangman(canvas,6-count)
       
        
        disp = ''        
        for ele in letters:
            disp = disp+ele
        label.config(text=disp)
    if count == 0:   
        label.config(text="Nope, better luck next time" + f"The correct answer is : {random_fruit}")
        draw_hangman(canvas,6)
    btn.config(text='Exit', command=quit)

def draw_hangman(canvas, incorrect_guesses):
    # Draw scaffold
    canvas.create_line(20, 200, 100, 200)
    canvas.create_line(60, 200, 60, 20)
    canvas.create_line(60, 20, 150, 20)
    canvas.create_line(150, 20, 150, 50)

  
    canvas.create_oval(135, 50, 165, 80)

    if incorrect_guesses >1:
        # Draw body
        canvas.create_line(150, 80, 150, 140)

    if incorrect_guesses >2:
        # Draw left arm
        canvas.create_line(150, 100, 120, 120)

    if incorrect_guesses >3:
        # Draw right arm
        canvas.create_line(150, 100, 180, 120)

    if incorrect_guesses >4:
        # Draw left leg
        canvas.create_line(150, 140, 130, 180)

    if incorrect_guesses >5:
        # Draw right leg
        canvas.create_line(150, 140, 170, 180)

        
def next():
    label.config(text = f'''So {name}, in this game you have guess the name of the fruit, whoes length matches the given spaces. 
    The fruit name will picked from our list of 50 fruits, randomly.
    You can have 6 incorrect guesses
    All the best!''')
    btn.config(text='START', command=start)

fruits = [
    "apple", "banana", "orange", "grape", "strawberry",
    "kiwi", "watermelon", "pineapple", "mango", "pear",
    "peach", "plum", "cherry", "blueberry", "raspberry",
    "blackberry", "lemon", "lime", "coconut", "pomegranate",
    "apricot", "fig", "avocado", "cantaloupe", "nectarine",
    "grapefruit", "dragonfruit", "passionfruit", "guava", "papaya",
    "lychee", "jackfruit", "cranberry", "tangerine", "aplle",
    "banana", "orange", "grape", "strawberry", "kiwi",
    "watermelon", "pineapple", "mango", "pear", "peach",
    "plum", "cherry", "blueberry", "raspberry", "blackberry"
]




# the gui window
app = tk.Tk()
# frame = tk.Frame(app)
# frame.pack(expand=True)
canvas = tk.Canvas(app,width=200,height=220)
canvas.pack()
label  = tk.Label(app,text='Hangman')
label.pack()
btn = tk.Button(app, text="Hello", command=get_name)
btn.pack() 
app.mainloop()

