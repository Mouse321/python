from pycat.core import Window, Sprite, Color
from random import randint

window = Window()
s = window.create_sprite()


class Bat(Sprite):
    def on_create(self):
        s.image = "bat-b.png"
        self.goto_random_position()

s1 = window.create_sprite(Bat)
s2 = window.create_sprite(Bat)
s3 = window.create_sprite(Bat)
for i in range(200):
    s = window.create_sprite(Bat)
    s.opacity = 200
    s.color = Color.random_rgb()
    s.rotation = randint(0,360)
    s.width = randint(0,10)
    s.height = randint(5,10)




window.run()