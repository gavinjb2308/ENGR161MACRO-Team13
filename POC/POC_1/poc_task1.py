from buildhat import Motor
from basehat import LineFinder
import time

def main():
	# For this code, please plug the motors into ports A, B, and C on the buildhat.
	# The line finder uses 
	motorOne = motor('A')
	motorTwo = motor('B')
	motorThree = motor('C')
	linePin = 16

	lineFinder = LineFinder(linePin)
	direction = 0
	while True:
		sensor_value = lineFinder.value
		print(f"lineFinder value: {sensor_value}, Direction: {direction}")
		
				
			
