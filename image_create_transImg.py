
from PIL import Image, ImageDraw

img = Image.new('RGBA', (198, 72), (255, 0, 0, 0))

draw = ImageDraw.Draw(img)

img.save('test.png', 'PNG')