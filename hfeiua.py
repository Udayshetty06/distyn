from machine import Pin
import time
trigger_pin=5
echo_pin=18
a=Pin(2,Pin.OUT)
trigger=Pin(trigger_pin,Pin.OUT)
echo=Pin(echo_pin,Pin.IN)
def distance():
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    
    while echo.value() == 0 :
        pass
    pulse_start=time.ticks_us()
    
    while echo.value() == 1:
        pass
    pulse_end = time.ticks_diff(pulse_end, pulse_start)
    distance_cm=(pulse_duration * 34300)/(2 * 1000000)
    return distance_cm
while True:
    dist=distance()
    if dist>=5 :
        a.value(1)
    else :
        a.value(0)
        
    time.sleep(1)
    

# new instrtcution 