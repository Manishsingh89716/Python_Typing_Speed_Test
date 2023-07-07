#Task 1(Golden_project):- Typing speed test in python

#import all necessary libraries
from tkinter import *
import random
from timeit import default_timer

#this module provide classes and functions for comapring purposes
import difflib

print("--------Python Typing Speed Test---------")

#define the geometry of window.
root = Tk()
root.title('Typing test')
root.geometry("400x400")
entered = StringVar()
welc = Label(root, font=('arial', 30, 'bold'), text="Welcome!")
welc.grid(row=0, columnspan=3)

#create random sentences, which will picked up by random module at any instant.
words = ["The way of success is the way of continuous pursuit of knowledge.",
        "More gold had been mined from the mind of men than the earth it self.",
        "We refuse to believe that which we don't understand."]
word = random.choice(words)

#create function for time-check.
def check():
    global entered
    global word
    global start

    string = f"{entered.get()}"
    end = default_timer()
    time = round(end - start, 2)
    print(time)
    speed = round(len(word.split()) * 60 / time, 2)
    print(speed)

#if given sentence equal to typed sentence.
    if string == word:
        Msg1 = "Time= " + str(time) + ' seconds'
        Msg2 = " Accuracy= 100% "

        #words per minute
        Msg3 = " Speed= " + str(speed) + 'word per min'

#if given sentence is not equal to typed sentence.
    else:
        accuracy = difflib.SequenceMatcher(None, word, string).ratio()
        accuracy = str(round(accuracy * 100, 2))
        Msg1 = "Time= " + str(time) + ' seconds'
        Msg2 = " Accuracy= " + accuracy + '%'

        # words per minute
        Msg3 = " Speed= " + str(speed) + ' word per min'

    label = Label(root, font=('arial', 15, 'bold'), text=Msg1)
    label.grid(row=7, columnspan=3)

    label = Label(root, font=('arial', 15, 'bold'), text=Msg2)
    label.grid(row=8, columnspan=3)

    label = Label(root, font=('arial', 15, 'bold'), text=Msg3)
    label.grid(row=9, columnspan=3)

#create function which asks user to enter or typed the given sentence.
def type():
    global word
    global start
    global entered

#create label or boxes for text area
    label = Label(root, font=('arial', 15), text="Type here")
    label.grid(row=5, column=1)

    entered = StringVar()
    enter = Entry(root, textvariable=entered, font=('arial', 15), width=20)
    enter.grid(row=5, column=3)

    btn = Button(root, text="Check", command=check, bg="DodgerBlue2", fg="white", font=('arial', 10))
    btn.grid(row=6, columnspan=6)

#create label for start the typing test
label = Label(root, font=('arial', 20, 'bold'), text=word)
label.grid(row=3, columnspan=3)

btn = Button(root, text=" Start typing", command=type, bg="DodgerBlue2", fg="white", font=('arial', 10))
btn.grid(row=4, columnspan=6)
start = default_timer()

#exit from window or closing the window
mainloop()

