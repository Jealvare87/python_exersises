import RPi.GPIO as GPIO
import time
from numpy import binary_repr as np

cont = 0
final = [0,0,0,0]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT) #1 
GPIO.setup(16,GPIO.OUT) #2
GPIO.setup(13,GPIO.OUT) #3
GPIO.setup(11,GPIO.OUT) #4


while True:
	#imprimir
	final = np(cont, width=4)

	GPIO.output(15, int(final[0]))
	GPIO.output(16, int(final[1]))
	GPIO.output(13, int(final[2]))
	GPIO.output(11, int(final[3]))
	
	time.sleep(1)
	cont = (cont+1) % 16
