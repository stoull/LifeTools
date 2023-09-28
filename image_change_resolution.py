import os
from PIL import Image

# 移除当前文件夹下图片中，包含的所有透明像素

# Absolute path to this script
scriptdir = os.path.dirname(os.path.abspath(__file__))

# Walk through directory
for root, subfolders, files in os.walk(scriptdir):
    for file in files:
        try:
            image = Image.open(os.path.join(scriptdir, root, file))
            # Save pasted image as image
            bg.save(os.path.join(scriptdir, root, file), "PNG", ppi=(72,72))
        except:
            pass