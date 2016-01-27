"""
picture.py
Author: Avery Wallis
Credit: None so far

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


red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xC4CACC, 1.0)


thinline= LineStyle(1, black)
thickline= LineStyle(5, black)
thickishline= LineStyle(2.5, black)
noline=LineStyle(0, black)

linedivide=LineAsset ([(250,20), (250,750)], thinline, black)
wall=RectangleAsset(500,500, noline, wall)
blueportal=ElllipseAsset(20,60,thinline,blue))


Sprite(wall, (400,20))
Sprite(wall, (100,20))
Sprite(blueportal, (200,200))


myapp = App()
myapp.run()
