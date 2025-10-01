import turtle as trtl
#trtl shapes for animals
#trtl.addshape("trotters"((-4,0),(-2,-4),(0,0),(2,-4),(4,0)))
#animal_parts = ["trotters"]
#Choose animal
animals = ["Pig", "Rat", "Chicken"]

#ask what animal they want
animal_chosen = input("Pig, Rat, or Chicken?")

if animal_chosen == "Pig":
 #Body
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
 trtl.penup()
 trtl.goto(-25,160)
 trtl.pendown()
 trtl.circle(8)
 
 

 
 












wn = trtl.Screen()
wn.mainloop()