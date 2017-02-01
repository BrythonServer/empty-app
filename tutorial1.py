from ggame import App
myapp = App()
myapp.run()
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xf8f8ff, 1.0)
yellow = Color(0xffff00, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
ylwln = LineStyle(1, yellow)
# A graphics asset that represents a rectangle
frnt = RectangleAsset(200, 100, thinline, black)
cntr = RectangleAsset(200,100, thinline, white)
back = RectangleAsset(200,100, thinline, black)
toprim = RectangleAsset(200, 100, thinline, white)
wndw = RectangleAsset(190, 90, thinline, blue)
alarm = EllipseAsset(35, 25, thinline, red)
crcle = CircleAsset(25, thinline, black)
star = PolygonAsset([(20,0),(0,34.641),(-20,0)], ylwln, yellow)
star2 = PolygonAsset([(20,0),(0,-34.641),(-20,0)], ylwln, yellow)
handle = RectangleAsset(50, 
# Now display a rectangle
Sprite(crcle, (600,580))
Sprite(crcle, (1000,580))
Sprite(frnt, (500,480))
Sprite(cntr, (700,480))
Sprite(back, (900,480))
Sprite(toprim, (700,380))
Sprite(wndw, (705, 385))
Sprite(alarm, (800,355))
Sprite(star, (800, 530))
Sprite(star2, (800, 548))

myapp = App()
myapp.run()