#basic servo motor test with PWM

import machine
import time, math

'''
p12 = machine.Pin(12)
pwm12 = machine.PWM(p12)

pwm12.freq(500)
pwm12.duty(512) # duty cycle is between 0 (all off) and 1023 (all on), with 512 being a 50% duty
'''
'''
# fading LED
def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)


led = machine.PWM(machine.Pin(14), freq=1000)
for _ in range(10):
    pulse(led,100)
'''
# hobby servo
servo = machine.PWM(machine.Pin(14), freq=50)
# 0/140 grad = 41/111 duty
# delta duty 70 = 140
# duty = angle/2 +41 

for angle in [0, 120, 30, 90, 45, 130, 80 , 110, 0]:
    servo.duty(int(angle/2) + 45)
    time.sleep(0.5)