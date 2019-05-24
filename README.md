# micropython-microbit-kitronik-klip-motor
Example MicroPython (for BBC micro:bit) code for the Kitronik Klip Motor Driver ( www.kitronik.co.uk/5655 )

## Overview

This repo contains a class for controlling motors and an example of a MicroPython program for the Kitronik Klip Motor Driver.
As well as the motor driving functions in the class, normal use of the 'microbit' and 'neopixel' libraries is required.

## 'KitronikKlipMotor' Class Functions

The 'motorOn' function takes the following parameters:
	(Motor to control, Motor Direction, Motor Speed)
The choice of motor can be "Motor1" or "Motor2", which correspond to the M1 and M2 markings on the Klip Motor Driver board outputs.
The motor can be given either "forward" or "reverse" directions (these are just relative to each other).
The motor speed is given as a percentage, from "0" to "100".
The function then turns on the selected motor, turning in the given direction at the chosen speed.

The 'motorOff' function takes the following parameters:
	(Motor to control)
The choice of motor can be "Motor1" or "Motor2".
The function then turns off the selected motor.

## Example Program

The file 'kitronikklipmotor.py' contains a simple program which sets a single ZIP LED to be red, drives two motors
and uses the BBC micro:bit buttons to control Pin outputs.

Any ZIP LEDs attached to the can be controlled in the usual way with the 'neopixel' library.
The only specific requirement is that the LEDs must be setup to connect to Pin 8 on the BBC micro:bit, as shown in the example:

zip_leds = neopixel.NeoPixel(pin8, 5)

The example program turns on the third ZIP LED in a string of 5 to be red at 50% brightness.

Then, continuing forever, Motor 1 will turn forwards at 100% speed for 1 second before turning off, 
and then Motor 2 will turn in reverse at 50% for 1 second before turning off.

Also within this loop are two if statements which check to see whether the BBC micro:bit buttons are pressed.
Pressing button a will set the output of Pins 0, 1 and 2 to be digital high, and button b will set them to digital low.

## License

MIT

## Supported Targets

BBC micro:bit
