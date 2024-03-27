# itsybitsyweather
 - pinouts are stated in the code
 - weather station shows temperature, pressure, humidity, and altitude
 - fonts must be located in /fonts
## Parts Used
 - Adafruit Itsybitsy M4 microcontroller
 - BME 280 temperature/pressure/humidity/altitude sensor
 - 2" ST7789 TFT display

## Pinouts
<code>
This test will initialize the Adafruit 128x128 display using displayio
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

</code>

   
