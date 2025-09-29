import turtle as trtl
#trtl shapes for animals
trtl.addshape("trotters"((-4,0),(-2,-4),(0,0),(2,-4),(4,0)))
#animal_parts = ["trotters"]
#Choose animal
animals = ["Pig", "Rat", "Chicken"]

#ask what animal they want
animal_chosen = input("Pig, Rat, or Chicken?")

if animal_chosen == "Pig":
  t = trtl.Turtle("trotters")
  t.forward(50)












wn = trtl.Screen()
wn.mainloop()