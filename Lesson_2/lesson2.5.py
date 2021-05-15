from pycat.window import Window

window = Window()

s = window.create_sprite()
s.image = "bat-b.png"
 
x = input("Enter bat position: ")

s.x = int(x)
s.y = 300







window.run()