from pycat.core import Window, Sprite, KeyCode

window = Window()



class bat(Sprite):
    def on_create(self):
        self.image = 'bat.png'
        self.y = 50


    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.D):
            self.move_forward(100)
            if self.is_touching_window_edge():
                self.move_forward(-100)
                self.rotation += 90


class Pico(Sprite):
    def on_create(self):
        self.image = 'pico.png'
        self.y = 100


    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.D):
            self.move_forward(100)
            if self.is_touching_window_edge():
                self.move_forward(-100)
                self.rotation += 90
                
                # window.close()




window.create_sprite(bat)
window.create_sprite(Pico)
window.run()
