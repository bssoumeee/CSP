# TODO Starting screen with title and bird and start button and set up leaderboard
# TODO Set up the background, the bird and the pillars
# TODO Code the key presses for the bird to flap
# TODO End screen with scores if you die
import turtle as trtl
wn = trtl.Screen()
wn.bgpic("flappyburd.gif")

#Setup
start_button = trtl.Turtle()
start_button.shape("square")
start_button.color("Yellow")
start_button.penup()
start_button.goto(0,-35)


trtl.addshape("tube",((-20, 210), (20, 210), (20, 60), (-20, 60),(-20, -60), (20, -60), (20, -210), (-20, -210)))
trtl.addshape("Bird", ((0,3), (2,3), (3,2), (3,1), (4,1), (5,0), (4,-1), (3,-1), (2,-2), (0,-3), (-2,-3), (-4,-2), (-5,-1), (-5,1), (-4,2), (-3,3)))
Burd = trtl.Turtle(shape="Bird")
Burd.hideturtle()
Burd.penup()
Burd.goto(-180,0)
Burd.left(90)
Burd.shapesize(5)
Burd.color("yellow")

Tube = trtl.Turtle(shape="tube")
Tube.hideturtle()
Tube.penup()
Tube.shapesize(2)
Tube.color("lime green")
Tube.left(90)
Tube.goto(60,10)

def fall(x,y):
    Burd.forward(4)
    Burd.speed(1)

def game_start(x,y):
    start_button.hideturtle()
    Burd.showturtle()
    Tube.showturtle()
  

while game_start == True:
    fall




start_button.onclick(game_start)








wn.mainloop()

