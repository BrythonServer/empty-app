from ggame import App
myapp = App()
myapp.run()
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0xf08080, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xf8f8ff, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
frnt = RectangleAsset(200, 100, thinline, black)
cntr = RectangleAsset(200,100, thinline, white)
back = RectangleAsset(200,100, thinline, black)
toprim = RectangleAsset(200, 100, thinline, white)
wndw = RectangleAsset(190, 90, thinline, blue)
# Now display a rectangle
Sprite(frnt, (500,480))
Sprite(cntr, (700,480))
Sprite(back, (900,480))
Sprite(toprim, (700,380))
Sprite(wndw, (700, 380))

myapp = App()
myapp.run()