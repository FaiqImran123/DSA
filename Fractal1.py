import turtle
import random

def f1(t):
    angle =90
    t.speed(200)
    color =["red","purple","black","green","blue","cyan"]
    while True:
        t.fillcolor(color[random.randint(0,5)])
        vone =random.randint(0,255)
        vtwo =random.randint(0,255)
        vthree =random.randint(0,255)
        t.pencolor(vone,vtwo,vthree)
        #t.fillcolor(color[random.randint(0,5)])
        #t.begin_fill()
        t.rt(angle)
        t.forward(90)
        #t.stamp()
        t.rt(90)
        t.forward(90)
        t.rt(90)
        #t.stamp()
        t.forward(90)
        #t.stamp()
        t.rt(90)
        t.forward(90)
        #t.stamp()
        # t.end_fill()
        angle +=1
def main1():
        turtle.getscreen()
        turtle.colormode(255)
        t =turtle.Turtle()
        turtle.bgcolor("white")
  

        f1(t)

main1()