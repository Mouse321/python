from pycat.core import Window

window = Window()
pico = window.create_sprite()
pico.scale = 1
pico.image = "pico-c.png"
pico.x = 150
pico.y = 150

squirt = window.create_sprite()
squirt.scale = 1
squirt.image = "squirrel.png"
squirt.x = 1125
squirt.y = 200

star = window.create_sprite()
star.scale = 1
star.image = "starfish.png"
star.x = 0
star.y = 1200

window.run()
