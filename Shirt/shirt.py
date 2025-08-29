import sys
import os.path
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Two command-line arguments expected")

ext_1 = os.path.splitext(sys.argv[1])[1]
ext_2 = os.path.splitext(sys.argv[2])[1]

if ext_1 not in [".jpg", ".jpeg", ".png"] and ext_2 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Expected .jpg/.jpeg or .png files")

if ext_1 != ext_2:
    sys.exit("Files must have the same extension")

try:
    muppet = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("File not found")

muppet = ImageOps.fit(muppet, shirt.size)
muppet.paste(shirt, mask=shirt)
muppet.save(sys.argv[2])
