from pycat.core import Window, Sprite, Scheduler
import random

window = Window(background_image='underwater_04.png', enforce_window_limits=False)
class UFO(Sprite):

    def on_create(self):
        self.image = 'saucer.png'
        self.y = 550
        self.scale = 0.4

    def on_update(self, dt):
        if self.x > window.width:
            self.rotation += 180
        if self.x < 0:
            self.rotation -= 180
        self.move_forward(10)
       
class Alien(Sprite):
    
        def on_create(self):
            self.image = '1.png'
            self.scale = 0.4
            self.x = 500
            self.y = 50
            self.is_on_ground = True

        def on_update(self, dt):
            if not self.is_on_ground:
                self.y += 10
                if self.y > window.height:
                    self.delete()
                if self.is_touching_sprite(ufo):
                    self.delete()
        
        def on_left_click(self):
            self.is_on_ground = False



def my_custom_update(dt):
    s3 = window.create_sprite(Alien)
    s3.x = random.randint(0, window.width)



Scheduler.update(my_custom_update, delay=2)

ufo = window.create_sprite(UFO)
window.run()