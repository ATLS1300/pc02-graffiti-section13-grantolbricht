#!/usr/bin/env python
# coding: utf-8
import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
t=turtle
t.shape("turtle")
t.circle(90)
t.pensize(10)
t.rt(90)
t.fd(100)
t.goto(-100,-200)
t.goto(-200,-200)
t.goto(0,0)
t.penup()
t.pensize(15)
t.goto(111,-90)
t.pendown()
t.fd(200)
t.penup()
t.goto(250,-100)
t.pendown()
t.pen(fillcolor="red", pensize=1)
t.begin_fill()
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(25)
t.end_fill()
t.penup()
t.goto(-15,100)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(25)
t.end_fill()
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
