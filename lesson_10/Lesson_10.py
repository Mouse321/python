from pycat.base import color
from pycat.core import Window, Sprite
import random
from typing import List

w = Window()



class Particle(Sprite):

    def on_create(self):
        self.scale = 10
        self.set_random_color()
        self.goto_random_position()
        self.rotation = random.randint(0,360)
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.rotation += 180

p: List[Particle] = []
for i in range(60):
    p.append(w.create_sprite(Particle))



    


class ColorButton(Sprite):

    def on_create(self):
        self.scale = 25
        self.y = 100

    def on_left_click(self):
        for i in range(len(p)):
            p[i].color = self.color
        
class Create(Sprite):

    def on_create(self):
        self.scale = 25
        self.y = 100
        self.x = 400

    def on_left_click(self):
        for i in range(4):
            p.append(w.create_sprite(Particle))


class Delete(Sprite):

    def on_create(self):
        self.scale = 25
        self.y = 100
        self.x = 600

    def on_left_click(self):
        for i in range(len(p)):
            p[i].delete()


w.create_sprite(ColorButton,
                x=200,
                color=(0, 0, 255))

w.create_sprite(ColorButton,
                x=100,
                color=(0, 255, 0))
w.create_sprite(ColorButton,
                x=300,
                color=(255, 0, 0))
w.create_sprite(Create)
w.create_sprite(Delete)
w.run()