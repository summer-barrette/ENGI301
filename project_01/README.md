# MOOD-DRAWING ROBOT

Hackster Project can be found at 
https://www.hackster.io/projects/949c22/edit#story

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


# PARTS LIST

*   1 Pocket Beagle
*   1 Adafruit Si7021 Temperature & Humidity Sensor
*   1 SG90 Micro-Servo Motor
*   1 L293x Quadruple Half-H Drivers
*   2 DC Gear Motors with Smart Car Robot Plastic Tire Wheel
*   2 Buttons (Yellow and Blue)
*   2 LEDs (Yellow and Blue)
*   2 1KΩ Resistors
*   2 10KΩ Resistors
*   1 0.1μF Capacitor
*   1 Solderless Breadboard (Half)
*   Assorted Jumper Wires
*   1 Pen Ink Cartridge
*   1 Wooden Dowel


# BUILD INSTRUCTIONS

*   Power Rail 1
    * Connect power rail 1 to PocketBeagle P1_14 (3.3 V).
*   Ground Rail 1
    * Connect ground rail 1 to PocketBeagle P1_16 (GND).
*   Yellow Button
    * Connect one pin both to PocketBeagle P2_2 (GPIO) and to a 1KΩ pullup 
      resistor (that is connected to power rail 1).
    * Connect other pin to ground rail 1.
*   Yellow LED
    * Connect anode to PocketBeagle P2_4 (GPIO).
    * Connect cathode to ground rail 1.
*   Temperature Sensor
    * Connect VIN pin both to a 0.1μF Capacitor (that is connected to ground) 
      and to power rail 1.
    * Connect GND pin to ground rail 1.
    * Connect SCL pin both to PocketBeagle P1_28 (SCL) and to a 10KΩ pullup 
      resistor (that is connected to power rail 1).
    * Connect SDA pin both to PocketBeagle P1_26 (SCL) and to a 10KΩ pullup 
      resistor (that is connected to power rail 1).
*   Blue Button
    * Connect one pin both to PocketBeagle P2_6 (GPIO) and to a 1KΩ pullup 
        resistor (that is connected to power rail 1).
    * Connect other pin to ground rail 1.
*   Blue LED
    * Connect anode to PocketBeagle P2_8 (GPIO).
    * Connect cathode to ground rail 1.
*   Servo
    * Connect VCC pin to PocketBeagle P1_24 (5V VOUT).
    * Connect GND pin to PocketBeagle P1_22 (GND).
    * Connect SIGNAL pin to PocketBeagle P1_36 (PWM0).
*   Power Rail 2
    * Connect power rail 2 to PocketBeagle P1_7 (5V VIN).
*   Ground Rail 2
    * Connect ground rail 2 to PocketBeagle P1_15 (GND)
*   Motor Driver and Left/Right Motor
    * Connect VCC2 and VCC1 pins to power rail 2.
    * Connect four GND pins to ground rail 2.
    * Connect 1,2EN pin to PocketBeagle P1_33 (GPIO).
    * Connect 1A pin to PocketBeagle P1_31 (GPIO).
    * Connect 1Y pin to right motor red wire.
    * Connect 2Y pin to right motor black wire.
    * Connect 2A pin to PocketBeagle P1_29 (GPIO).
    * Connect 3,4EN pin to PocketBeagle P1_30 (GPIO).
    * Connect 3A pin to PocketBeagle P1_32 (GPIO).
    * Connect 3Y pin to left black motor wire.
    * Connect 4Y pin to left motor red wire.
    * Connect 4A pin to PocketBeagle P1_34 (GPIO).
*   Chassis
    * Laser cut chassis vector template out of foam core
    * Using hot glue, assemble foam chassis so that 
    * (first) the wheels and back wooden dowel are between levels 1 and 2.
    * (second) the PocketBeagle and servo are between levels 2 and 3.
    * (third) the solderless breadboard is above level 3.
    * (fourth) the front wooden dowel and pencil go from the ground to above 
      level 2.
    * Tie the servo to the pen with a thin wire; ensure servo pushes pen down 
      into the ground when ‘on’ and pulls pen up off the ground when ‘off’
      

# OPERATION INSTRUCTIONS

1.  Run the command ./run in the command line to run the run script
2.	Press the yellow button while either covering or not covering the 
    temperature sensor
    * The yellow LED should turn on
    * The temperature should be recorded and the mood (happy or sad) decided
    * The yellow LED should turn off
3.	Set the robot in the center of a standard sheet of letter paper
    * (first) the paper is in a vertical orientation.
    * (second) the wooden dowel is on the top left corner of the paper.
    * (third) the front of the robot is facing and parallel to the top edge 
      of the paper.
4.	Press the blue button
    * The blue light should come on
    * The robot should drive around while picking up and putting down the pen
    * The robot should draw a frowny or smiley face
5.	The ‘temperature’ function and ‘drawing’ function do not have to be linear. 
    This means the temperature can be re-recorded by hitting the yellow button 
    directly after the previous temperature sequence. And the robot can re-draw 
    the same smiley or frowny face by hitting the blue button directly after 
    the previous drawing sequence.