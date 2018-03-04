#basic main function to reset the pins and start the main function of the ESP8266
import machine
import time
import led
'''
Reset aller Pins auf low
starten des Arbeitsmoduls
'''


def reset_pins():
    # pin_list = [0, 2, 4, 5, 12, 13, 14, 15, 16]
    PIN_LIST = [5, 12, 13, 14, 15, 16]

    for nr in PIN_LIST:
        pin = machine.Pin(nr, machine.Pin.OUT)
        pin.low()


def func_led_test():
    # Pinbelegung am Board
    PIN_RED = 15
    PIN_GREEN = 12
    PIN_BLUE = 14
    DELAY = 0.5
    for i in range(5):
        led.led_test([PIN_RED, PIN_GREEN, PIN_BLUE], DELAY)
        time.sleep(DELAY)


#Abbruch Main(), wenn Pin 14 auf high()
#exit main(), if pin 14 is high() - use jumerwire to stop auto-mode
reset_pins()
PIN_CANCEL = machine.Pin(14, machine.Pin. IN)
if not PIN_CANCEL.value():
    func_led_test()
