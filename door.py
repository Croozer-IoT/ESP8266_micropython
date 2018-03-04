#basic demo for door sensor
import machine

pinDOOR = machine.Pin(14, machine.Pin.IN)
pinRED = machine.Pin(13, machine.Pin.OUT)
pinGREEN = machine.Pin(12, machine.Pin.OUT)
pinRED.low()
pinGREEN.low()

for:
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
