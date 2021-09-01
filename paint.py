import turtle
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import random
from random import randint
root = tk.Tk()
turtle.onscreenclick(turtle.goto)
root.geometry('375x300')
colors = ["Red","Orange", "Yellow", "Green", "Blue", "Purple"]
print("""
  _____        _____ _   _ _______ 
 |  __ \ /\   |_   _| \ | |__   __|
 | |__) /  \    | | |  \| |  | |   
 |  ___/ /\ \   | | | . ` |  | |   
 | |  / ____ \ _| |_| |\  |  | |   
 |_| /_/    \_\_____|_| \_|  |_|

Version: 3.3
Paint Action Logs:
""")

def r():
    turtle.color("red")
    print("Color changed to: Red")
    print("----------------------")
def o():
    turtle.color("orange")
    print("Color changed to: Orange")
    print("----------------------")
def y():
    turtle.color("yellow")
    print("Color changed to: Yellow")
    print("----------------------")
def g():
    turtle.color("green")
    print("Color changed to: Green")
    print("----------------------")
def b():
    turtle.color("blue")
    print("Color changed to: Blue")
    print("----------------------")
def p():
    turtle.color("purple")
    print("Color changed to: Purple")
    print("----------------------")
def w():
    turtle.color("white")
    print("Color changed to: White")
    print("----------------------")
def bl():
    turtle.color("black")
    print("Color changed to: Black")
    print("----------------------")
def undo():
    turtle.undo()
    print("Action undone!")
    print("----------------------")
def bgr():
    turtle.bgcolor("red")
    print("Background color changed to: Red")
    print("----------------------")
def bgo():
    turtle.bgcolor("orange")
    print("Background color changed to: Orange")
    print("----------------------")
def bgy():
    turtle.bgcolor("yellow")
    print("Background color changed to: Yellow")
    print("----------------------")
def bgg():
    turtle.bgcolor("green")
    print("Background color changed to: Green")
    print("----------------------")
def bgb():
    turtle.bgcolor("blue")
    print("Background color changed to: Blue")
    print("----------------------")
def bgp():
    turtle.bgcolor("purple")
    print("Background color changed to: Purple")
    print("----------------------")
def bgw():
    turtle.bgcolor("white")
    print("Background color changed to: White")
    print("----------------------")
def bgbl():
    turtle.bgcolor("black")
    print("Background color changed to: Black")
    print("----------------------")
def clear():
    turtle.clear()
    print("Cleared!")
    print("----------------------")
def credit():
    mb.showinfo("Credits", "Created By: Alex")
def pensize():
    size = sd.askinteger("Pen Size", "Set Size", parent=root)
    turtle.pensize(size)
    print("Pensize changed to: " + str(size))
    print("----------------------")
def pensizereset():
    turtle.pensize(1)
    print("Pensize reset.")
    print("----------------------")
def penup():
    turtle.penup()
    print("Stop drawing.")
    print("----------------------")
def pendown():
    turtle.pendown()
    print("Started drawing.")
    print("----------------------")
def bfill():
    turtle.begin_fill()
    print("Started filling.")
    print("----------------------")
def efill():
    turtle.end_fill()
    print("Stopped filling.")
    print("----------------------")
def randomize():
    color = random.choice(colors)
    
    turtle.color(color)
    randomsize = randint(1,50)
    turtle.pensize(randomsize)
    
    randombg = random.choice(colors)
    turtle.bgcolor(randombg)
    print("Randomizing...")
    print("Pen color changed to: " + color)
    print("Background color changed to: " + randombg)
    print("Pen size changed to: " + str(randomsize))
    print("----------------------")
def turtlereset():
    turtle.goto(0,0)
    turtle.bgcolor("White")
    turtle.pensize(1)
    turtle.color("Black")
    turtle.clear()
    print("Screen has been reset.")
    print("----------------------")
Label(root, text="Colors").grid(row=1,column=1)
Label(root, text="Background Color").grid(row=1,column=2)
Label(root, text="Pen Options").grid(row=1,column=3)
Label(root, text="Other/Misc").grid(row=1,column=4)

tk.Button(root,text = 'Red', command=r,pady=5,padx=5).grid(row=2,column=1)
tk.Button(root,text = 'Orange', command=o,pady=5,padx=5).grid(row=3,column=1)
tk.Button(root,text = 'Yellow', command=y,pady=5,padx=5).grid(row=4,column=1)
tk.Button(root,text = 'Green', command=g,pady=5,padx=5).grid(row=5,column=1)
tk.Button(root,text = 'Blue', command=b,pady=5,padx=5).grid(row=6,column=1)
tk.Button(root,text = 'Purple', command=p,pady=5,padx=5).grid(row=7,column=1)
tk.Button(root,text = 'White', command=w,pady=5,padx=5).grid(row=8,column=1)
tk.Button(root,text = 'Black', command=bl,pady=5,padx=5).grid(row=9,column=1)

tk.Button(root,text = 'Red', command=bgr,pady=5,padx=5).grid(row=2,column=2)
tk.Button(root,text = 'Orange', command=bgo,pady=5,padx=5).grid(row=3,column=2)
tk.Button(root,text = 'Yellow', command=bgy,pady=5,padx=5).grid(row=4,column=2)
tk.Button(root,text = 'Green', command=bgg,pady=5,padx=5).grid(row=5,column=2)
tk.Button(root,text = 'Blue', command=bgb,pady=5,padx=5).grid(row=6,column=2)
tk.Button(root,text = 'Purple', command=bgp,pady=5,padx=5).grid(row=7,column=2)
tk.Button(root,text = 'White', command=bgw,pady=5,padx=5).grid(row=8,column=2)
tk.Button(root,text = 'Black', command=bgbl,pady=5,padx=5).grid(row=9,column=2)

tk.Button(root,text = 'Pen Size', command=pensize,pady=5,padx=5).grid(row=2,column=3)
tk.Button(root,text = 'Pen Size Reset', command=pensizereset,pady=5,padx=5).grid(row=3,column=3)
tk.Button(root,text = 'Pen Up',command=penup,pady=5,padx=5).grid(row=4,column=3)
tk.Button(root,text = 'Pen Down',command=pendown,pady=5,padx=5).grid(row=5,column=3)

tk.Button(root,text = 'Clear',command=clear,pady=5,padx=5).grid(row=2,column=4)
tk.Button(root,text = 'Undo', command=undo,pady=5,padx=5).grid(row=3,column=4)
tk.Button(root,text = 'Reset',command=turtlereset,pady=5,padx=5).grid(row=4,column=4)
tk.Button(root,text = 'Begin Fill',command=bfill,pady=5,padx=5).grid(row=5,column=4)
tk.Button(root,text = 'Finish Fill',command=efill,pady=5,padx=5).grid(row=6,column=4)
tk.Button(root,text = 'Randomize',command=randomize,pady=5,padx=5).grid(row=7,column=4)
tk.Button(root,text = 'Credits', command=credit,pady=5,padx=5).grid(row=8,column=4)


turtle.listen()
