import RPi.GPIO as GPIO
import time

def servoMotorControl():
	servo = 18
	button = 19
	led = 5

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servo, GPIO.OUT)
	GPIO.setup(button, GPIO.IN)
	GPIO.setup(led, GPIO.OUT)

	servoMotor = GPIO.PWM(servo, 50)
	servoMotor.start(0)

	left_angle = 12.5
	center_angle = 7.5
	right_angle = 2.5

	try:
		while True:
			if (GPIO.input(button) == 0):
				servoMotor.ChangeDutyCycle(right_angle)
				print("Button Pressed")
				time.sleep(5)
				GPIO.output(led, 1)
				time.sleep(0.5)
			else :
				servoMotor.ChangeDutyCycle(left_angle)
				print("Button Released")
				GPIO.output(led, 0)
				time.sleep(0.5)
	except KeyboardInterrupt:
		servoMotor.stop()
		GPIO.cleanup()
