#basic demo with PIR motion sensor
import machine
"""
PIR via 4,5V anschließen (rot und schwarz)
gelb als IN an huzzah
schwarz mit GND huzzah verbinden
"""

pinPIR = machine.Pin(14, machine.Pin.IN)
pinRED = machine.Pin(13, machine.Pin.OUT)
pinGREEN = machine.Pin(12, machine.Pin.OUT)
pinRED.low()
pinGREEN.low()

while True:
    if pinPIR.value():
        pinRED.high()
        pinGREEN.low()
    else:
        pinRED.low()
        pinGREEN.high()
"""
pinRED.low()
pinGREEN.low()
print('end')
"""
