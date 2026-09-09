# created on Sept 9
# making LED on connected device blink green

#include module
#module with all the microcontroller stuff
import machine 
#module with time methods
import time

#assigns object by calling the built in pin function and defining its parameters for the green LED
#Green LED is GPIO Pin 0
led = machine.Pin(0,machine.Pin.OUT)

#endless loop to make the light blink
while True:
  #turns LED on
  led.value(1)

  #waits 0.25 seconds
  time.sleep(0.25)
  
  #turns LED off
  led.value(0)

  #waits 0.25 seconds
  time.sleep(0.25)
  