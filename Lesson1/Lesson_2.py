from pycat.core import Window
window = Window()
animal = window.create_sprite()
anwser = input("What animal do you like?")
animal.x = 620
animal.y = 320


if anwser == "pico":
    animal.image = "pico-c.png"

if anwser == "squirrel":
    
    animal.image = "squirrel.png"

if anwser == "starfish":
    animal.image = "starfish.png"

if anwser == "cat":
    animal.image = "Cat.png"
anwser0 = input("Do you want your animal big or small?")
 
if anwser0 == "big":
    animal.scale = 10

if anwser0 == "small":
    animal.scale = 0.5





window.run()
