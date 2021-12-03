# MOOD-DRAWING ROBOT

Hackster Project can be found at 
https://www.hackster.io/summer-barrette/mood-drawing-robot-949c22.

# STORY

My project is a mood-drawing robot. The project was inspired by the idea of 
mood rings, which are fun accessories that change color based on the 
temperature around them. My robot contains a temperature sensor that is able to 
use body heat to distinguish between times when the user is not covering the 
sensor and times when the user is covering the sensor. The robot then decides 
either that it is that it is happy (the user was covering the sensor) or sad 
(the user was not covering the sensor). Finally, using wheels connected to the 
chassis and a pen connected to a servo, the robot moves around and draws the 
user a corresponding smiley or frowny face on a standard sheet of letter paper.

# PRINTED CIRCUIT BOARD DESIGN

This repository contains the files necessary for manufacturing a printed circuit 
board for the Mood-Drawing Robot. 
*   "robot docs" contains (1) the original proposal, (2) schematics as a PDF, 
    (3) top and bottom assembly views with associated dimensions, (4) a bill of
    materials, and (5) previews of the top and bottom layer Gerber files.
*   "robot eagle" contains all the Eagle files used to build the printed circuit
    board design including (1) library of components, (2) schematics, (3) design
    rules, and (4) layout of the board.
*   "robot mfg" contains all manufacturing files including Gerber files.


# PARTS LIST

*   1 Pocket Beagle
*   1 SG90 Micro-Servo Motor
*   1 L293x Quadruple Half-H Drivers
*   2 DC Gear Motors with Smart Car Robot Plastic Tire Wheel
*   2 Buttons (Yellow and Blue)
*   1 Pen Ink Cartridge
*   1 Wooden Dowel

*   1 Printed Ciruit Board with
    * 1 Adafruit Si7021 Temperature & Humidity Sensor
    * 2 LEDs (Yellow and Blue)
    * 2 1KΩ Resistors
    * 2 10KΩ Resistors
    * 1 0.1μF Capacitor


# BUILD INSTRUCTIONS

*   Solder Through-hole Components
    * Solder PocketBeagle to PocketBeagle Outline
    * Solder Adafruit Si7021 Temperature & Humidity Sensor to U3 Outline
    * Solder L293x Quadruple Half-H Drivers to U2 Outline
    * Solder SG90 Micro-Servo Motor wires to U4 power, signal, and ground pads
    * Solder DC Gear Motors to M1 and M2 power and ground pads
*   Construct Chassis
    * Laser cut chassis vector template out of foam core
    * Using hot glue, assemble foam chassis so that 
    * (first) the wheels and back wooden dowel are between levels 1 and 2.
    * (second) the PocketBeagle and servo are between levels 2 and 3.
    * (third) the solderless breadboard is above level 3.
    * (fourth) the front wooden dowel and pen go from the ground to above 
      level 2.
    * Tie the servo to the pen with a thin wire; ensure servo pushes pen down 
      into the ground when ‘on’ and pulls pen up off the ground when ‘off’.


# OPERATION INSTRUCTIONS

1.  Turn on PocketBeagle to run the run script
    * The pins should be configured.
    * The program should initialize.
2.	Press the yellow button while either covering or not covering the 
    temperature sensor
    * The yellow LED should turn on.
    * The temperature should be recorded and the mood (happy or sad) decided.
    * The yellow LED should turn off.
3.	Set the robot in the center of a standard sheet of letter paper
    * (first) the paper is in a vertical orientation.
    * (second) the wooden dowel is on the top left corner of the paper.
    * (third) the front of the robot is facing and parallel to the top edge 
      of the paper.
4.	Press the blue button
    * The blue light should come on.
    * The robot should drive around while picking up and putting down the pen.
    * The robot should draw a frowny or smiley face.
5.	The ‘temperature’ function and ‘drawing’ function do not have to be linear. 
    This means the temperature can be re-recorded by hitting the yellow button 
    directly after the previous temperature sequence. And the robot can re-draw 
    the same smiley or frowny face by hitting the blue button directly after 
    the previous drawing sequence.
