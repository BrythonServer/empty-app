from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
noline = LineStyle(1, red)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(500, 500, thinline, blue)
circle = CircleAsset(200, thinline, red)
eyes = EllipseAsset(50, 30, thinline, Color(0x073d91, 1.0))
pupils = EllipseAsset(20, 30, thinline, Color(0xffffff, .8))
mouth = EllipseAsset(100, 50, thinline, Color(0x008000, 1.0))
mouth2 = EllipseAsset(100, 40, noline, red)
triangle = PolygonAsset([(270,270), (330,270), (300,250), (270,270)], thinline, black)
teeth = PolygonAsset([(260,345), (280,345), (270,360), (260,345)], thinline, Color(0xffffff, 1.0))
# Now display a rectangle
Sprite(rectangle, (50,30))
Sprite(circle, (300, 250))
Sprite(eyes, (240, 200))
Sprite(eyes, (370, 200))
Sprite(mouth, (300, 320))
Sprite(mouth2, (300, 305))
Sprite(triangle, (0, 0))
Sprite(pupils, (240, 200))
Sprite(pupils, (370, 200))
Sprite(teeth, (0,0))
myapp = App()
myapp.run()
