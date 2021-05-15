from pycat.core import Window, Sprite, KeyCode

window = Window(background_image='img/sea.png')

class Player(Sprite):
    def on_create(self):
        self.image = 'img/ork1.png'
        self.scale = 0.1


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


class UpDown(Sprite):

    def on_create(self):
        self.image = "img/owl.png"
        self.rotation = 90


    def on_update(self, dt):

        self.move_forward(5)
        if self.is_touching_window_edge():
            self.rotation += 180


class Round(Sprite):

    def on_create(self):
        self.image = "img/owl.png"
        self.rotation = 90


    def on_update(self, dt):

        self.move_forward(5)
        self.rotation += 10

player=window.create_sprite(Player)

class Follow(Sprite):

    def on_create(self):
        self.image = "img/owl.png"
        self.point_toward_sprite(player)


    def on_update(self, dt):
        self.point_toward_sprite(player)
        self.move_forward(5)
            

window.create_sprite(UpDown, x=500, y=550)
window.create_sprite(UpDown, x=250, y=300)
window.create_sprite(Round, x=500, y=550)
window.create_sprite(Round, x=250, y=300)
window.create_sprite(Follow, x=1000, y=1000)





window.run()
