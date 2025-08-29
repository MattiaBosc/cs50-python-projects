from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = fonts[random.randint(0, len(fonts)-1)]
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Font not found")
else:
    sys.exit("Zero or two line commands expected")

figlet.setFont(font=font)
text = input("Input: ")
print(figlet.renderText(text))

