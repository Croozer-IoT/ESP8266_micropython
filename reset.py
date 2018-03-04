#reset modul to low all pins
import machine
import time

def reset_pin_low():
    #pin_list = [0, 2, 4, 5, 12, 13, 14, 15, 16]
    pin_list = [13, 12]
    for nr in pin_list
        pin = machine.Pin(nr, machine.Pin.Out)
        pin.low()
        time.sleep(1.0)
        pin.high()
        time.sleep(1.0)
        pin.low()
