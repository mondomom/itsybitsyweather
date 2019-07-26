"""
This test will initialize the display using displayio
and display weather information on a teal background
with "WEATHER" in red

WIRING
------
ST7735      ITSYBITSY M4
Vin         3V
3.3V        n/c
GND         G
SCK         SCK
MISO        n/c
MOSI        MO
TFT_CS      D9
RST         D11
D/C         D10
CARD_CS     n/c
LITE        n/c

BME280(i2c) ITSYBITSY M4
VIN         3V
GND         GND
SCK         SCL
SDI         SDA

"""

import board
import displayio
import terminalio
import time
import busio
import adafruit_bme280
from adafruit_bitmap_font import bitmap_font
from adafruit_st7735R import ST7735R
from adafruit_display_text.label import Label

spi = board.SPI()
tft_cs = board.D9
tft_dc = board.D10
HEAD_STRING = "WEATHER"
displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D11)

display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)
# load the heading font
large_font_name = "/fonts/Arial-12.bdf"
large_font = bitmap_font.load_font(large_font_name)
large_font.load_glyphs(HEAD_STRING.encode('utf-8'))
# Make the display context
splash = displayio.Group(max_size=20)
display.show(splash)

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x73c6b7
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

#spi2 = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bme_cs = digitalio.DigitalInOut(board.D12)
# bme_cs = board.D12
#bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi2, bme_cs)
# bme280 = Adafruit_BME280_SPI(spi, bme_cs)
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1021.10
# set up strings, 2 decimal places

TEMP_STRING = "Temp:  " + str(round(bme280.temperature, 2)) + "C"
HUMID_STRING = "Humidity: " + str(round(bme280.humidity, 2)) + "%"
PRESS_STRING = "Pressure: " + str(round((bme280.pressure/10), 2)) + "kPa"
ALT_STRING = "Altitude: " + str(round(bme280.altitude, 2)) + "M"
BACKGROUND_TEXT_COLOR = 0xFFFFFF
HEADING_BACKGROUND = 0xFF0000
font = terminalio.FONT
heading_label = Label(large_font, text=HEAD_STRING, color=0x00FF00)
(x, y, w, h) = heading_label.bounding_box
heading_label.x = 5
heading_label.y = 10
heading_label.color = HEADING_BACKGROUND
splash.append(heading_label)
temp_label = Label(font, text=TEMP_STRING, color=0x00FF00)
(x, y, w, h) = temp_label.bounding_box
temp_label.x = 5
temp_label.y = 30
temp_label.color = BACKGROUND_TEXT_COLOR
splash.append(temp_label)
humid_label = Label(font, text=HUMID_STRING, color=0x00FF00)
(x, y, w, h) = humid_label.bounding_box
humid_label.x = 5
humid_label.y = 45
humid_label.color = BACKGROUND_TEXT_COLOR
splash.append(humid_label)
pressure_label = Label(font, text=PRESS_STRING, color=0x00FF00)
(x, y, w, h) = pressure_label.bounding_box
pressure_label.x = 5
pressure_label.y = 60
pressure_label.color = BACKGROUND_TEXT_COLOR
splash.append(pressure_label)
altitude_label = Label(font, text=ALT_STRING, color=0x00FF00)
(x, y, w, h) = altitude_label.bounding_box
altitude_label.x = 5
altitude_label.y = 75
altitude_label.color = BACKGROUND_TEXT_COLOR
splash.append(altitude_label)
print("Hello, ItsyBitsy")
while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    TEMP_STRING = "Temp:  " + str(round(bme280.temperature, 2)) + "C"
    HUMID_STRING = "Humidity: " + str(round(bme280.humidity, 2)) + "%"
    PRESS_STRING = "Pressure: " + str(round((bme280.pressure/10), 2)) + "kPa"
    ALT_STRING = "Altitude: " + str(round(bme280.altitude, 2)) + "M"
    #pop(temp_label.text)
    temp_label.text = TEMP_STRING
    humid_label.text = HUMID_STRING
    pressure_label.text = PRESS_STRING
    altitude_label.text = ALT_STRING
    time.sleep(2)
    pass
