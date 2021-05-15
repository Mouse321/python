from pycat.core import Window, Sprite, AudioLoop, Player
from random import shuffle
from typing import List


clicked_sprite: List['Card'] = []
window = Window(draw_sprite_rects=True, background_image= 'forest_04.png')
music = AudioLoop('LoopLivi.wav')
music.play()
hit_a_card = Player('hit.wav')
dont_match = Player('laugh.wav')
match = Player('point.wav')

class Mycheckbutton(Sprite):

    def on_create(self):
        self.x = 1000
        self.y = 500
        self.scale = 0.5
        self.image = 'button.png'

    def on_left_click(self):
        if len(clicked_sprite) == 2:
            a = clicked_sprite[0]
            b = clicked_sprite[1]
            if a.image == b.image:
                a.is_rotating = True
                b.is_rotating = True
                match.play()
            else:
                dont_match.play()
                a.is_visible = False
                b.is_visible = False
            clicked_sprite.clear()
               





class Card(Sprite):

    def on_create(self):
        self.is_visible = False
        self.y = 100
        self.is_rotating = False
    def on_left_click(self):
        if len(clicked_sprite) < 2:
            self.is_visible = True
            if self not in clicked_sprite:
                clicked_sprite.append(self)
                hit_a_card.play()
            print(clicked_sprite)

    def on_update(self, dt):
        if self.is_rotating:
            self.rotation += 7
            if self.rotation > 360:
                self.delete()
            
for y in range(500, 99, -100):

    img_list = 2 * ["1.png", "2.png", "3.png", "4.png"]
    shuffle(img_list)
    for i in range(len(img_list)):
        card = window.create_sprite(Card)
        card.image = img_list.pop()
        card.x = 100 + i*100
        card.y = y





window.create_sprite(Mycheckbutton)
window.run()
