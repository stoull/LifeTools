import os
from PIL import Image

# 将当前文件夹下图片裁剪到400px以内，并压缩

# Absolute path to this script
scriptdir = os.path.dirname(os.path.abspath(__file__))

# Walk through directory
for root, subfolders, files in os.walk(scriptdir):
    for file in files:
        try:
            image = Image.open(os.path.join(scriptdir, root, file))
            width, hight = image.size
            print(f'{width} {hight} : {file}')
            if width > 400:
                coefficient = width / 400
                new_hight = hight / coefficient
                new_hight = round(new_hight)
                image = image.resize((400, new_hight), Image.ANTIALIAS)
            elif hight > 400:
                oefficient2 = hight / 400
                new_width = width / oefficient2
                new_width = round(new_width)
                image = image.resize((new_width, 400), Image.ANTIALIAS)
            image.save(os.path.join(scriptdir, root, file), quality=80, optimize=True)
        except:
            print("except")
            pass