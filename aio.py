# weather measurment - dht.py and publish to io.adafruit dashboard
import network
import time
import machine
import dht
from umqtt.simple import MQTTClient

# Exit Main(), if pin 14 is high()
Pin_cancel = machine.Pin(14, machine.Pin. IN)
if not Pin_cancel.value():

    # init LED
    pin_red = 15
    pin_green = 12
    LED_red = machine.Pin(pin_red, machine.Pin. OUT)
    LED_green = machine.Pin(pin_green, machine.Pin. OUT)
    LED_red.high()
    LED_green.low()

    # init DHT
    DHT_DELAY = 1
    weather = dht.DHT22(machine.Pin(13))
    for i in range(10):
        try:
            weather.measure()
            break
        except:
            # print('Fehler init {0:0.0f}'.format(i))
            time.sleep(DHT_DELAY)  # sensor refresh

    # print('init erfolgreich nach {0:0.0f}'.format(i))
    time.sleep(DHT_DELAY)  # sensor refresh

    # connect the ESP8266 to local wifi network
    WiFi_SSID = 'YOUR SSID'
    WiFi_pwd = 'YOUR KEY'
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(WiFi_SSID, WiFi_pwd)
    while not sta_if.isconnected():
        pass

    # print('WiFi connection {0} status {1}'.format(sta_if.isconnected(),
    # sta_if.status()))

    # connect ESP8266 to Adafruit IO using MQTT
    myMqttClient = 'ANY'  # can be anything unique
    Aio_Url = 'io.adafruit.com'
    Aio_username = 'YOUR USERNAME'
    Aio_key = 'YOUR KEY'
    c = MQTTClient(myMqttClient, Aio_Url, 0, Aio_username, Aio_key)
    #dashboard design has to be equal to the publish statments

    Mqtt_connected = c.connect()
    LED_red.low()
    # print('MQTT connection status ' + str(Mqtt_connected))
    # print ('MQTT connected {0}'.format(c.connect()))

    # print('WiFi connection {0} status {1}'.format(sta_if.isconnected(),
    # sta_if.status()))
    LED_green.high()

    for i in range(30):
        # messung
        messung_io = False
        for i in range(2):
            try:
                weather.measure()
                # print('Messung {0:0.0f} erfolgreich'.format(i))
                time.sleep(DHT_DELAY)  # sensor refresh
                # weather.humidity()
                # weather.temperature()
                # print('Luftfeuchte: {0:0.1f}%  Temperatur: {1:0.1f}C {2}'
                # .format(weather.humidity(), weather.temperature()))
                time.sleep(4)  # Warten bis nächste Messung
                messung_io = True
            except:
                # print('Fehler bei Messung')
                pass

        if messung_io:
            LED_red.high()
            c.publish(
                '{0}/feeds/temperatur'.format(Aio_username),
                '{0}'.format(weather.temperature()))
            c.publish(
                '{0}/feeds/feuchte'.format(Aio_username),
                '{0}'.format(weather.humidity()))
            LED_red.low()
        time.sleep(120)  # number of seconds between each publish

    c.disconnect()
    sta_if.disconnect()
    LED_green.low()
    LED_red.low()
