from microbit import *
import neopixel

class KitronikKlipMotor:
    # Function to control the turning on of motors
    # Each motor can have different direction and speed
    def motorOn(self, motor, direction, speed):
        
        if speed > 100:
            speed = 100
        elif speed < 0:
            speed = 0
        speed = speed * 10
        if motor == "Motor1":
            if direction == "forward":
                pin15.write_analog(speed)
                pin16.write_digital(0)
            elif direction == "reverse":
                pin16.write_analog(speed)
                pin15.write_digital(0)
        elif motor == "Motor2":
            if direction == "forward":
                pin13.write_analog(speed)
                pin14.write_digital(0)
            elif direction == "reverse":
                pin14.write_analog(speed)
                pin13.write_digital(0)

    # Function to control the turning off of motors
    def motorOff(self, motor):
        if motor == "Motor1":
            pin15.write_digital(0)
            pin16.write_digital(0)
        elif motor == "Motor2":
            pin13.write_digital(0)
            pin14.write_digital(0)
        
# Create a new instance of the Klip Motor class
klip = KitronikKlipMotor
# Setup a string of 5 ZIP LEDs attached to the Klip Motor board
# NOTE: ZIP LEDs must be connected to Pin 8 on the BBC micro:bit
zip_leds = neopixel.NeoPixel(pin8, 5)
# Set the 3rd ZIP LED in the string to be red and turn it on
zip_leds[2] = (128, 0, 0)
zip_leds.show()

while True:
    # Drive Motor 1 forward at 100% speed for 1s, then turn off
    klip.motorOn(klip, "Motor1", "forward", 100)
    sleep(1000)
    klip.motorOff(klip, "Motor1")
    # Drive Motor 2 in reverse at 50% speed for 1s, then turn off
    klip.motorOn(klip, "Motor2", "reverse", 50)
    sleep(1000)
    klip.motorOff(klip, "Motor2")
    # Check to see if BBC micro:bit button a is pressed
    # If it is pressed, write the Pin0, 1 and 2 outputs to be digital 1
    if button_a.is_pressed():
        pin0.write_digital(1)
        pin1.write_digital(1)
        pin2.write_digital(1)
    # Check to see if BBC micro:bit button b is pressed
    # If it is pressed, write the Pin0, 1 and 2 outputs to be digital 0
    if button_b.is_pressed():
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)