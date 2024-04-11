 #!/usr/bin/env python
# -*- coding: utf-8 -*-

# libraries
import time
import RPi.GPIO as GPIO

red = 12
blue = 6

GPIO_TRIGGER=18
GPIO_ECHO=19

# led pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


#ultrasound sensor
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use Pins 18,22,24,26 GPIO24,GPIO25,GPIO8,GPIO7
#StepPins = [24,25,8,7]
StepPins = [4,17,22,23]

# Set all pins as output
for pin in StepPins:
        # print(pin, "Setup pins")
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)

# Define values
waitTime = 0.002
stepCount = 512
direction = False

#grey code
stepSequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
                 
# clean up
def cleanup():
  for pin in StepPins:
    GPIO.output(pin, False)
  GPIO.cleanup()

def run(steps): #counter clockwise
  for i in range(steps):
    for step in range(len(stepSequence)):
      for pin in range(len(StepPins)):
        GPIO.output(StepPins[pin], stepSequence[step][pin])
        # print("send signal", StepPins[pin], stepSequence[step][pin])
      time.sleep(waitTime)

def run_clockwise(steps): #clockwise
  reversed_spin = stepSequence[::-1]
  for i in range(steps):
    for step in range(len(stepSequence)):
      for pin in range(len(StepPins)):
        GPIO.output(StepPins[pin], reversed_spin[step][pin])
        # print("send signal", StepPins[pin], stepSequence[step][pin])
      time.sleep(waitTime)

 
 
def distance():
	#set trigger to high
	GPIO.output(GPIO_TRIGGER,True)
	
	#set trigger after 0.01ms to low
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER,False)
	
	StartTime = time.time()
	StopTime = time.time()
	#save start time
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	#print("HEY")
		
	#save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
		
	#print("HEY2")
	
	#time difference between start an arrival
	TimeElapsed = StopTime - StartTime
	
	#print("HEY3")
	
	#multiply with sonic speed (34300cm/s)
	distance=(TimeElapsed * 34300)/2
	#and divide by 2 because there and back
	return distance

 
if __name__ == '__main__' :
  try:
    while True:
      print('Rotate by 12 degree')
      #rotate()

      dist = distance()
      print("distance is " + str(dist))

      if dist > 30:
        GPIO.output(blue, True)
        GPIO.output(red, False)
        #rotate()
        print("Counter clockwise")
        run(100)

      else:
        GPIO.output(blue, False)
        GPIO.output(red, True)
        time.sleep(.5)
        GPIO.output(red, False)
        time.sleep(.5)
        GPIO.output(red, True)
        time.sleep(.5)
        GPIO.output(red, False)
        time.sleep(.5)
        GPIO.output(blue, False)
        print("Clockwise")
        run_clockwise(100)
        #cleanup()


      time.sleep(1)
  except KeyboardInterrupt:
      GPIO.cleanup()	

