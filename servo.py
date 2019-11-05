import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
top = 12.0

def setservo(servo,rad):
    duty=(rad+90)*4.7/90+2.5
    servo.changeDutyCycle(duty)


GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
servo=GPIO.PWM(2,50)
servo.start(0.0)

for i in range(5):
    setservo(servo,-90)
    time.sleep(1.0)
    setservo(servo,0)
    time.sleep(1.0)
    setservo(servo,90)
    time.sleep(1.0)



