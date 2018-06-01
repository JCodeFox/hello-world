from turtle import *
import random
b=["red","green","blue"]
a=Turtle()
a.speed(0)
a.pu()
a.goto(0,-200)
a.pd()
for i in range(3600):
    a.lt(i)
    a.color(b[i%len(b)])
    a.fd(i/180)
