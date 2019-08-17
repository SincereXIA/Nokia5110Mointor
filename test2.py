import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi software SPI config:
_SCLK = 17
_DIN = 18
_DC = 27
_RST = 23
_CS = 22

# LCD config
_CONTRAST = 60  #对比度 0-127


# Software SPI usage (defaults to bit-bang SPI interface):
_disp = LCD.PCD8544(_DC, _RST, _SCLK, _DIN, _CS)

# Initialize library.
_disp.begin(contrast=60)

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
_image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Clear display.
_disp.clear()
_disp.display()

draw = ImageDraw.Draw(_image)
_disp.image(_image)
_disp.display()
