#basic demo of a DHT22 sensor
import dht
import machine
import time

DHT_DELAY = 1

weather = dht.DHT22(machine.Pin(13))
for i in range(10):
    try:
        weather.measure()
        break
    except:
        #print('error init {0:0.0f}'.format(i))
        time.sleep(DHT_DELAY) #sensor refresh
print('init successful after {0:0.0f} loops'.format(i))
time.sleep(DHT_DELAY) #sensor refresh

#10 measurements with 5 seconds delay
for i in range(2):
    try:
        weather.measure()
        #print('measurement {0:0.0f} successful'.format(i))
        time.sleep(DHT_DELAY) #sensor refresh
        #weather.humidity()
        #weather.temperature()
        print('humidity: {0:0.1f}%  temperature: {1:0.1f}C'.format(weather.humidity(), weather.temperature()))
        time.sleep(5) #wait for next measuremet
    except:
        print('measurement error')
