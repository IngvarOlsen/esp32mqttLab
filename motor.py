from machine import Pin
from time import sleep
import umqtt_robust2
lib = umqtt_robust2

relay = Pin(26, Pin.OUT)
speed = 0.5

mqtt_pub = bytes(
    "{:s}/feeds/{:s}".format(b'ingv0351', b'bot_pub'), "utf-8")
mqtt_sub = bytes(
    "{:s}/feeds/{:s}".format(b'ingv0351', b'bot_sub'), "utf-8")

def adaConnect():
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            lib.c.reconnect()
            pass
        else:
            lib.c.resubscribe()
            lib.c.publish(topic=mqtt_pub, msg="Connection test")
            pass
    
while True:
    adaConnect()
    lib.c.wait_msg()
    if(lib.getSubMessage() == "gardin op"):
        relay.value(1)
        sleep(10)
        relay.value(0)
        
    
    

    
        
#     relay.value(1)
#     sleep(speed)
#     relay.value(0)
#     sleep(speed)
#     print("test")