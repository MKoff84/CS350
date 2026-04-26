import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Create PWM instance on GPIO18 at 60 Hz
pwm18 = GPIO.PWM(18, 60)

# Start PWM at 0% duty cycle
pwm18.start(0)

try:
    while True:

        # Fade LED brighter
        for dutyCycle in range(0, 101, 5):
            pwm18.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)

        # Fade LED dimmer
        for dutyCycle in range(100, -1, -5):
            pwm18.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

# Cleanup when Ctrl+C is pressed
pwm18.stop()
GPIO.cleanup()
