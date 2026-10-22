from buildhat import Motor
from basehat import LineFinder
import time

def main():
	# For this code, please plug the motors into ports A, B, and C on the buildhat.
	# The line finder uses 
	motorLeft = motor('A')
	motorRight = motor('B')
	motorFront = motor('C')
	linePin = 16

	lineFinder = LineFinder(linePin)
	direction = 0
	while True:
		sensor_value = lineFinder.value
		print(f"lineFinder value: {sensor_value}, Direction: {direction}")

		if sensor_value == 0:
			if direction == 0:
				motorLeft.start(10)
				motorRight.start(-10) # the right turn 
				motorFront.start() # this one should just drive unless stopped
				direction = 1
			elif direction > 0:
				if direction > 10:
					direction += 1
				else: 
					direction = -1
					motorLeft.start(-10)
					motorRight.start(10)
					motorFront.start()
			else:
				if direction > 10:
					direction -= 1
				else:
					direction = 1
					motorLeft.start(10)
					motorRight.start(-10)
					motorFront.start() 
		else:
			direction = 0
			motorLeft.start()
			motorRight.start()
			motorFront.start()
		time.sleep(0.1)

if __name__ == "__main__":
	main()
			
				
			
