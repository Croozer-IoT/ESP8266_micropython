#basic demo with RGB-Led
import machine
import time

"""
3V mit 560 Ohm an Anonde (lang)
Pins an Kathoden - pin.low() = GND = an
"""
led_red = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(12, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)
led = [led_red, led_green, led_blue]

for i in range(3):
    led[i].high()   # high = ground --> on bei 3Farb-LED

# time.sleep(2.0)

for i in range(3 * 10):
    led[i % 3].low()
    time.sleep(0.2)
    led[i % 3].high()
