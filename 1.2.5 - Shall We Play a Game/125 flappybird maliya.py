# TODO Starting screen with title and bird and start button and set up leaderboard
# TODO Set up the background, the bird and the pillars
# TODO Code the key presses for the bird to flap
# TODO End screen with scores if you die
import turtle as trtl
#Setup
trtl.addshape("Bird", ((0,3), (2,3), (3,2), (3,1), (4,1), (5,0), (4,-1), (3,-1), (2,-2), (0,-3), (-2,-3), (-4,-2), (-5,-1), (-5,1), (-4,2), (-3,3)))
Burd = trtl.Turtle(shape="Bird")
Burd.left(90)
Burd.shapesize(5)
Burd.color("yellow")

start_button = trtl.Turtle()
start_button.shape("square")
start_button.color("Yellow")
start_button.penup()
start_button.goto(0,0)
start_button.write("Click to start", align="center", font=("Arial", 16, "bold"))




wn = trtl.Screen()
wn.mainloop()