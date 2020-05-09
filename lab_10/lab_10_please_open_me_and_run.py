# -*- coding: utf-8 -*-
import turtle
import time

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("light blue")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)

# draw sun
my_turtle.color("yellow")
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.setposition(150, 150)
my_turtle.begin_fill()
my_turtle.pendown()
my_turtle.circle(50)
my_turtle.end_fill()
# draw sun
my_turtle.color("orange")
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.setposition(150, 160)
my_turtle.begin_fill()
my_turtle.pendown()
my_turtle.circle(40)
my_turtle.end_fill()
# draw sun
my_turtle.color("red")
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.setposition(150, 170)
my_turtle.begin_fill()
my_turtle.pendown()
my_turtle.circle(30)
my_turtle.end_fill()

# draw rays
my_turtle.color("yellow")
my_turtle.penup()
my_turtle.goto(150, 140)
my_turtle.pendown()
my_turtle.goto(150, 130)
# I quad
my_turtle.penup()
my_turtle.goto(185 + 7, 165 - 7)
my_turtle.pendown()
my_turtle.goto(185 + 14, 165 - 14)

my_turtle.penup()
my_turtle.goto(210, 200)
my_turtle.pendown()
my_turtle.goto(220, 200)
# II quad
my_turtle.penup()
my_turtle.goto(185 + 7, 235 + 7)
my_turtle.pendown()
my_turtle.goto(185 + 14, 235 + 14)

my_turtle.penup()
my_turtle.goto(150, 260)
my_turtle.pendown()
my_turtle.goto(150, 270)

# III quad
my_turtle.penup()
my_turtle.goto(115 - 7, 235 + 7)
my_turtle.pendown()
my_turtle.goto(115 - 14, 235 + 14)

my_turtle.penup()
my_turtle.goto(90, 200)
my_turtle.pendown()
my_turtle.goto(80, 200)

# IV quad
my_turtle.penup()
my_turtle.goto(115 - 7, 165 - 7)
my_turtle.pendown()
my_turtle.goto(115 - 14, 165 - 14)

shift = 90

# draw lines
my_turtle.penup()
my_turtle.goto(-190, -180 - shift)
my_turtle.color("yellow")
my_turtle.pensize(7)
my_turtle.pendown()
my_turtle.goto(190, -180 - shift)

my_turtle.penup()
my_turtle.goto(-175, -165 - shift)
my_turtle.color("#FF1493")
my_turtle.pensize(7)
my_turtle.pendown()
my_turtle.goto(175, -165 - shift)

my_turtle.penup()
my_turtle.goto(-160, -150 - shift)
my_turtle.color("yellow")
my_turtle.pensize(7)
my_turtle.pendown()
my_turtle.goto(160, -150 - shift)

my_turtle.penup()
my_turtle.goto(-145, -135 - shift)
my_turtle.color("#FF1493")
my_turtle.pensize(7)
my_turtle.pendown()
my_turtle.goto(145, -135 - shift)

my_turtle.penup()
my_turtle.goto(-130, -120 - shift)
my_turtle.color("yellow")
my_turtle.pensize(7)
my_turtle.pendown()
my_turtle.goto(130, -120 - shift)

my_turtle.penup()
my_turtle.goto(-115, -105 - shift)
my_turtle.color("#FF1493")
my_turtle.pensize(7)
my_turtle.pendown()
my_turtle.goto(115, -105 - shift)

# draw cake
my_turtle.begin_fill()
my_turtle.penup()
my_turtle.goto(-75, -95 - shift)
my_turtle.pendown()
my_turtle.color("orange")
my_turtle.goto(75, -95 - shift)
my_turtle.left(90)
my_turtle.forward(40)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(40)
my_turtle.end_fill()
colours = "#4169E1", "#FFA500","#7B68EE","#BA55D3", "#FFFF00","#FF4500","#FF6347", "#1E90FF", "#00FF00"
for i in range(0, 16):
    my_turtle.penup()
    my_turtle.goto(-72 + (i * 9.5), -50 - shift)
    my_turtle.color(colours[i % len(colours)])
    my_turtle.pendown()
    my_turtle.pensize(3)
    my_turtle.goto(-72 + (i * 9.5), -35 - shift)
colours_of_fire = "#FFA500", "#FF8C00", "#FF4500","#FF6347"
for i in range(0, 16):

    my_turtle.penup()
    my_turtle.goto(-72 + (i * 9.5), -33 - shift)
    my_turtle.color("#FFA500")
    my_turtle.pendown()
    my_turtle.pensize(3)
    my_turtle.goto(-72 + (i * 9.5), -29 - shift)

for i in range(0, 16):
    # низ пламени
    my_turtle.penup()
    my_turtle.goto(-72 + (i * 9.5), -33 - shift)
    my_turtle.color("#4682B4")
    my_turtle.pendown()
    my_turtle.pensize(4)
    my_turtle.goto(-72 + (i * 9.5), -32 - shift)
    # сердинка пламени
    my_turtle.penup()
    my_turtle.goto(-72 + (i * 9.5), -31 - shift)
    my_turtle.color("#FF4500")
    my_turtle.pendown()
    my_turtle.pensize(5)
    my_turtle.goto(-72 + (i * 9.5), -29 - shift)
    # сердинка пламени
    my_turtle.penup()
    my_turtle.goto(-72 + (i * 9.5), -29 - shift)
    my_turtle.color("#FF4500")
    my_turtle.pendown()
    my_turtle.pensize(4)
    my_turtle.goto(-72 + (i * 9.5), -26 - shift)
    # сердинка пламени
    my_turtle.penup()
    my_turtle.goto(-72 + (i * 9.5), -28 - shift)
    my_turtle.color("#FF4500")
    my_turtle.pendown()
    my_turtle.pensize(3)
    my_turtle.goto(-72 + (i * 9.5), -25 - shift)

    # верхушка пламени
    my_turtle.penup()
    my_turtle.goto(-72 + (i * 9.5), -31 - shift)
    # my_turtle.color("#FFA500")
    my_turtle.color(colours_of_fire[i % len(colours_of_fire)])
    my_turtle.pendown()
    my_turtle.pensize(3)
    my_turtle.goto(-72 + (i * 9.5), -27 - shift)

# # draw candles
# my_turtle.penup()
# my_turtle.goto(-60, -65 - shift)
# my_turtle.color("aquamarine")
# my_turtle.pendown()
# my_turtle.pensize(3)
# my_turtle.goto(-60, -20 - shift)
#
# my_turtle.penup()
# my_turtle.goto(-40, -40 - shift)
# my_turtle.color("yellow")
# my_turtle.pendown()
# my_turtle.pensize(3)
# my_turtle.goto(-40, -20 - shift)
#
# my_turtle.penup()
# my_turtle.goto(-20, -40 - shift)
# my_turtle.color("green")
# my_turtle.pendown()
# my_turtle.pensize(3)
# my_turtle.goto(-20, -20 - shift)
#
# my_turtle.penup()
# my_turtle.goto(0, -40 - shift)
# my_turtle.color("pink")
# my_turtle.pendown()
# my_turtle.pensize(3)
# my_turtle.goto(0, -20 - shift)
#
# my_turtle.penup()
# my_turtle.goto(20, -40 - shift)
# my_turtle.color("blue")
# my_turtle.pendown()
# my_turtle.pensize(3)
# my_turtle.goto(20, -20 - shift)

# print message
my_turtle.penup()
my_turtle.goto(-330, 160 - shift)
my_turtle.color("grey")
my_turtle.pendown()
my_turtle.write(
    "С днём рождения, Наталия Артуровна!", move=False,
    font=("Helvetica", 24, "bold"))
# print message
my_turtle.penup()
my_turtle.goto(-330, 130 - shift)
my_turtle.color("grey")
my_turtle.pendown()
my_turtle.write(
    "Желаю вам оставаться такой-же доброй и красивой:)", move=False,
    font=("Helvetica", 18, "bold"))
# print message
my_turtle.penup()
my_turtle.goto(-330, 110 - shift)
my_turtle.color("grey")
my_turtle.pendown()
my_turtle.write(
    "Если вы всё-таки уйдёте с универа,", move=False,
    font=("Helvetica", 18, "bold"))
# print message
my_turtle.penup()
my_turtle.goto(-330, 90 - shift)
my_turtle.color("grey")
my_turtle.pendown()
my_turtle.write(
    "то удачи в новом деле - не лентяйничайте, как я)", move=False,
    font=("Helvetica", 18, "bold"))

# print message
my_turtle.penup()
my_turtle.goto(-330, 70 - shift)
my_turtle.color("grey")
my_turtle.pendown()
my_turtle.write(
    "Если останетесь с нами, то мы будем очень рады, ", move=False,
    font=("Helvetica", 18, "bold"))

# print message
my_turtle.penup()
my_turtle.goto(-330, 50 - shift)
my_turtle.color("grey")
my_turtle.pendown()
my_turtle.write(
    "Но вы не оставайтесь,  не надо;)", move=False,
    font=("Helvetica", 18, "bold"))

# print message
my_turtle.penup()
my_turtle.goto(-330, 30 - shift)
my_turtle.color("grey")
my_turtle.pendown()
my_turtle.write(
    "Сори за лагающий Python", move=False,
    font=("Helvetica", 18, "bold"))

# send the turtle to the corner
my_turtle.penup()
my_turtle.goto(-250, 250)
time.sleep(60)

# partially from https://pycoder.ru/happy-birthday-with-python-turtle/
