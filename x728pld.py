#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os

PLD_PIN = 6
BUZZER_PIN = 20
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PLD_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

seconds_without_power = 0

while True:
    i = GPIO.input(PLD_PIN)
    if i == 0:
        print("AC Power OK")
        GPIO.output(BUZZER_PIN, 0)
        seconds_without_power = 0
    elif i == 1:
        print("Power Supply A/C Lost")
        seconds_without_power += 1
        if seconds_without_power >= 10:
            GPIO.output(BUZZER_PIN, 1)
            time.sleep(0.1)
            GPIO.output(BUZZER_PIN, 0)
            time.sleep(1)
            os.system('/usr/local/bin/x728softsd.sh')

    time.sleep(1)
