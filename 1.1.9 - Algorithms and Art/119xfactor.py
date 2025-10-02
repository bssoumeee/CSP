import turtle as trtl
#trtl shapes for animals
#trtl.addshape("trotters"((-4,0),(-2,-4),(0,0),(2,-4),(4,0)))
#animal_parts = ["trotters"]
#Choose animal
animals = ["Pig", "Rat", "Chicken"]

#ask what animal they want
animal_chosen = input("Pig, or Chicken?")

if animal_chosen == "Pig":
 #Body
 trtl.speed(100)
 trtl.pencolor("pink")
 trtl.penup()
 trtl.goto(0,-80)
 trtl.pendown()
 trtl.circle(80)
 #Head
 trtl.penup()
 trtl.goto(0,70)
 trtl.pendown()
 trtl.circle(65)
 #Ears
 trtl.penup()
 trtl.goto(35,190)
 trtl.pendown()
 trtl.circle(15)
 trtl.penup()
 trtl.goto(-35, 190)
 trtl.pendown()
 trtl.circle(15)
 #Nose
 trtl.penup()
 trtl.goto(0,105)
 trtl.pendown()
 trtl.circle(15)
 trtl.penup()
 trtl.goto(-5,115)
 trtl.pendown()
 trtl.circle(5)
 trtl.penup()
 trtl.goto(5,115)
 trtl.pendown()
 trtl.circle(5)
 #Eyes
 trtl.color("black")
 trtl.penup()
 trtl.goto(-25,155)
 trtl.pendown()
 trtl.circle(8)
 trtl.penup()
 trtl.goto(25,155)
 trtl.pendown()
 trtl.circle(8)
 #Tail
# for i in range(60):
  #trtl.forward(50)
  #trtl.right(60)

if animal_chosen == "Chicken":
 #Body
 trtl.speed(100)
 trtl.penup()
 trtl.goto(0,-80)
 #trtl.color("yellow")
 trtl.pendown()
 trtl.circle(80)
 #Head
 trtl.penup()
 trtl.goto(0,70)
 trtl.pendown()
 trtl.circle(60)
 #eyes and nose

 trtl.penup()
 trtl.goto(-25,135)
 trtl.pendown()
 trtl.circle(12)
#trtl.pencolor("black")
 trtl.penup()
 trtl.goto(-25, 143)
 trtl.pendown()
 trtl.fillcolor("black")
 trtl.begin_fill()
 trtl.circle(4)
 trtl.end_fill()
 
 trtl.penup()
 trtl.goto(25,135)
 trtl.pendown()
 #trtl.pencolor("yellow")
 trtl.circle(12)
 trtl.pencolor("black")
 trtl.penup()
 trtl.goto(25, 143)
 trtl.pendown()
 trtl.fillcolor("black")
 trtl.begin_fill()
 trtl.circle(4)
 trtl.end_fill()

 trtl.penup()
 trtl.goto(0,120)
 trtl.pendown()
 trtl.circle(9)
 
#wings
trtl.penup()
trtl.goto(77,20)
trtl.pendown()
trtl.circle(28, 258)
 
trtl.penup()
trtl.goto(-53,60)
trtl.pendown()
trtl.setheading(120)
trtl.circle(28, 260)

#Head thingy













wn = trtl.Screen()
wn.mainloop()