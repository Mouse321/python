from pycat.core import Window, Sprite

w = Window()

my_list = [
        '1.jpg',
        '2.jpg',
        '3.jpg', 
        '4.jpg',
        '5.jpg']
text_list = ["bus", "bus stop", "bus_number2", "wood_plartform", "Plants"]
label = w.create_label()
label.text = text_list[0]

class Button(Sprite):

    def on_create(self):
        self.image = 'button_next.png'
        self.scale = 0.5
        self.x = w.width/2
        self.y = 200
        self.img_num = 0
    def on_left_click(self):
        self.img_num += 1
        if self.img_num ==  len(my_list):
            w.close()
            return
        w.background_image = my_list[self.img_num]
        label.text = text_list[self.img_num]

class Up(Sprite):

    def on_create(self):
        self.image = 'thumbs_up.png'
        self.scale = 0.5
        self.x = 900
        self.y = 500
    def on_update(self, dt):
        pass




w.background_image = my_list[0]


w.create_sprite(Button)
w.run()