from pycat.core import Window, Sprite, KeyCode

window = Window(background_image='img/sea.png')

class Player(Sprite):
    def on_create(self):
        self.image = 'img/owl.png'


    def on_update(self, dt):
        self.move_forward(10)
        if window.is_key_down(KeyCode.UP):
            self.rotation = 90
        if window.is_key_down(KeyCode.DOWN):
            self.rotation = 270
        if window.is_key_down(KeyCode.LEFT):
            self.rotation = 180
        if window.is_key_down(KeyCode.RIGHT):
            self.rotation = 0
        
        if self.x > 1225:
            print("You Win!")
            window.close()

        if self.is_touching_any_sprite():
            print("You Lose!") 
            window.close()       


s = window.create_sprite()
s.image = "img/beach.png"

s.x = 500
s.y = 550
window.create_sprite(Player)


window.create_sprite(image='img/beach.png',x=500, y=100)
window.create_sprite(image='img/beach.png',x=500, y=230)
window.create_sprite(image='img/beach.png',x=700, y=300)
window.create_sprite(image='img/beach.png',x=600, y=430)





window.run()
