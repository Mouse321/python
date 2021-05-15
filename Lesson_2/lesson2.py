from pycat.window import Window

window = Window()

s = window.create_sprite()
s.image = "bat-b.png"

s.x = 500
s.y = 220



print("The sprite is at the position(",s.x, s.y,")",s.image)







window.run()