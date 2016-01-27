"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
aqua = Color(0x00FFFF, 1.0) 
white = Color(0xFFFFFF, 1.0)
gold = Color(0xD4AF37, 1.0)
thinline = LineStyle(1, black)
thickline = LineStyle(3, red)

head = RectangleAsset(1000, 500, thickline, blue)
nose = CircleAsset(100, thinline, aqua)
eye1 = PolygonAsset([(0,0),(100,0),(125,50),(50,100),(-25,50)], thinline, green) 
eye2 = PolygonAsset([(0,0),(100,0),(125,50),(50,100),(-25,50)], thinline, green)
mouth1 = RectangleAsset(500,100, thickline, black)
dot1 = EllipseAsset(20,20, thinline, red) 
tooth1 = EllipseAsset(20,30, thinline, white)
tooth2 = EllipseAsset(20,30, thinline, white)
tooth3 = EllipseAsset(20,30, thinline, white)
tooth4 = EllipseAsset(20,30, thinline, white)
goldtooth = EllipseAsset(20,30, thinline, gold)

#  
Sprite(head)
Sprite(nose, (500, 277))
Sprite(eye1, (250, 100))
Sprite(eye2, (700,100))
Sprite(mouth1, (250,385))
Sprite(dot1, (220, 385))
Sprite(tooth1, (420, 415)) 
Sprite(tooth2, ( 580, 415))
Sprite(tooth3, ( 460, 415))
Sprite(tooth4, ( 540, 415))
Sprite(goldtooth, (500, 415))





myapp = App()
myapp.run()

# add your code here /\  /\  /\


myapp = App()
myapp.run()
