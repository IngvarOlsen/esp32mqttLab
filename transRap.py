from machine import Pin
from time import sleep_ms, sleep


relay = Pin(26, Pin.OUT)
relay.value(0)

speed = 0.001

while True:
    relay.value(1)
    sleep(speed)
    relay.value(0)
    sleep(speed)

while True:
    
    #Øvelse 5
#     relay.value(1)
#     sleep(0.5)
#     relay.value(0)
#     sleep(5)
    
    
    #Øvelse 6
    relay.value(0)
    sleep(speed)
    relay.value(1)
    sleep(speed)
    print("Test")
    
