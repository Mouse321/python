from pycat.core import Window, Sprite, KeyCode

window = Window()


class Bat(Sprite):
    def on_create(self):
        self.image = 'bat-b.png'
        self.y = 100


    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.A):
            self.x += 1
            if self.is_touching_window_edge():
                print("BAT WON!")
                window.close()




class Squirrel(Sprite):
    def on_create(self):
        self.image = 'squirrel.png'
        self.y = 500


    def on_update(self, dt):
        if window.is_key_up(KeyCode.S):
            self.x += 12
            if self.is_touching_window_edge():
                print("SQUIRREL WON!")
                window.close()


class Pico(Sprite):
    def on_create(self):
        self.image = 'pico.png'
        self.y = 300


    def on_update(self, dt):
        if window.is_key_down(KeyCode.D):
            self.move_forward(100)
            if self.is_touching_window_edge():
                self.rotation = 180
            
                # window.close()




            
window.create_sprite(Pico)
window.create_sprite(Squirrel)
window.create_sprite(Bat)
window.run()
