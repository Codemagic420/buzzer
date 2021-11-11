from machine import Pin
from time import sleep

button = Pin(4, Pin.IN)
buzzer = Pin(2, Pin.OUT, value=0)

while True:
    print("knap vaerdi: ", button.value())
    buzzer.value(not button.value())
    sleep(0.1)
