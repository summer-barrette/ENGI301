# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Mood-Drawing Robot
--------------------------------------------------------------------------
License:   
Copyright 2021 Summer Barrette

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

DESCRIPTION

- Requires Adafruit_CircuitPython_SI7021 Library
- Uses modified code originally taken from a previous student's repository:
  jae-kim-1107/ENGI301/project_1/motor_control.py
  
- Waits for either yellow button press or blue button press
- Upon yellow button press, temperature at temperature sensor is recorded
  and the value is sorted into a 'happy' or 'sad' category
- Upon blue button press, a combination of the wheel motors being driven 
  forward/backward and the servo attached to the pencil moving up/down
  allows the robot to draw either a smiley or frowny face based on sorted
  temperature category
- Button presses are non-linear. Yellow button can be pressed after a
  temperature sequence to rerecord temperature. Blue button can be
  pressed after a drawing sequence to redraw same smiley or frowny face.

--------------------------------------------------------------------------
"""

import time
import Adafruit_BBIO.GPIO as GPIO
import adafruit_si7021
from busio import I2C
from board import SCL_2, SDA_2
import Adafruit_BBIO.PWM as PWM

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

SG90_FREQ   = 50                  # 20ms period (50Hz)
SG90_POL    = 0                   # Rising Edge polarity
SG90_OFF    = 5                   # 0ms pulse -- Servo is inactive
SG90_RIGHT  = 5                   # 1ms pulse (5% duty cycle)  -- All the way right
SG90_LEFT   = 10                  # 2ms pulse (10% duty cycle) -- All the way Left

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

motor1 = ['P1_29', 'P1_31', 'P1_33']
motor2 = ['P1_34', 'P1_32', 'P1_30']

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Robot():
    """ Robot """
    
    yellow_button = None
    yellow_led = None
    blue_button = None
    blue_led = None
    servo = None
    
    
    def __init__(self,           \
        yellow_button="P2_2",    \
        yellow_led="P2_4",       \
        blue_button="P2_6",      \
        blue_led="P2_8",         \
        servo="P1_36"):
        
        self.yellow_button = yellow_button
        self.yellow_led    = yellow_led
        self.blue_button   = blue_button
        self.blue_led      = blue_led
        self.servo         = servo
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""
        
        # Initialize Buttons
        GPIO.setup(self.yellow_button, GPIO.IN)
        GPIO.setup(self.blue_button, GPIO.IN)
        
        # Initialize LEDs
        GPIO.setup(self.yellow_led, GPIO.OUT)
        GPIO.setup(self.blue_led, GPIO.OUT)
        
        # Initialize Servo; Servo should be "off"
        PWM.start(self.servo, SG90_OFF, SG90_FREQ, SG90_POL)
        
        # Initialize Right Motor
        GPIO.setup('P1_29',GPIO.OUT)
        GPIO.setup('P1_31',GPIO.OUT)
        GPIO.setup('P1_33',GPIO.OUT)
        
        # Initialize Left Motor
        GPIO.setup('P1_34',GPIO.OUT)
        GPIO.setup('P1_32',GPIO.OUT)
        GPIO.setup('P1_30',GPIO.OUT)
        
        # Enable Driver Channels
        GPIO.output('P1_33', 1)
        GPIO.output('P1_30', 1)
    
    # End def
    
    
    # def drive(self)
    """Drive the Motors"""
    
    def stop(self):
        GPIO.output('P1_29', 0)
        GPIO.output('P1_31', 0)
        GPIO.output('P1_34', 0)
        GPIO.output('P1_32', 0)
    # End def
    
    def setforward(self, motor):
        GPIO.output(motor[0], 1)
        GPIO.output(motor[1], 0)
    # End def
    
    def setbackward(self, motor):
        GPIO.output(motor[0], 0)
        GPIO.output(motor[1], 1)
    # End def
    
    def moveforward(self):
        self.setforward(motor=motor1)
        self.setforward(motor=motor2)
    # End def
    
    def movebackward(self):
        self.setbackward(motor=motor1)
        self.setbackward(motor=motor2)
    # End def
    
    def turnleft(self):
        self.setforward(motor=motor1)
    # End def
    
    def turnright(self):
        self.setforward(motor=motor2)
    # End def
    
    def turnsharpleft(self):
        self.setforward(motor=motor1)
        self.setbackward(motor=motor2)
    # End def
    
    def turnsharpright(self):
        self.setforward(motor=motor2)
        self.setbackward(motor=motor1)
    # End def
    
    # End def
    
    
    def run(self):
        """Execute the main program."""
        
        emotion = None                        # Initialize emotion
        yellow_button_press_time = 0.0        # Time yellow button was pressed (in seconds)
        blue_button_press_time   = 0.0        # Time blue button was pressed (in seconds)
        
        print("Program Start")
        
        while(1):
            
            # Wait for button press
            while (GPIO.input(self.yellow_button) == 1) and (GPIO.input(self.blue_button) == 1):
                pass
            
            # Yellow button pressed
            if (GPIO.input(self.yellow_button) == 0) and (GPIO.input(self.blue_button) == 1):
                
                # Record time
                yellow_button_press_time = time.time()
                
                # Wait for button release
                while(GPIO.input(self.yellow_button) == 0):
                    pass
                
                # Turn light on, measure temperature, turn light off
                if ((time.time() - yellow_button_press_time) > 0.0):
                    GPIO.output(self.yellow_led, GPIO.HIGH)
                    time.sleep(3)
                    
                    i2c = I2C(SCL_2, SDA_2)
                    sensor = adafruit_si7021.SI7021(i2c)
                    print("Temperature =", sensor.temperature)
                    
                    # Decide if happy or sad
                    if (sensor.temperature > 22):
                        emotion = "happy"
                    else:
                        emotion = "sad"
                    
                    print("I am", emotion)
                    
                    GPIO.output(self.yellow_led, GPIO.LOW)
            
            # Blue button pressed
            if (GPIO.input(self.yellow_button) == 1) and (GPIO.input(self.blue_button) == 0):
                
                # Record time
                blue_button_press_time = time.time()
                
                # Wait for button release
                while(GPIO.input(self.blue_button) == 0):
                    pass
                
                # Turn light on, draw shapes, turn light off
                if ((time.time() - blue_button_press_time) > 0.0):
                    
                    # Turn light on
                    GPIO.output(self.blue_led, GPIO.HIGH)
                    time.sleep(1)
                    
                    # Draw face
                    self.movebackward()
                    time.sleep(0.4)
                    self.stop()
                    time.sleep(1)
                    self.turnright()
                    time.sleep(0.5)
                    self.stop()
                    time.sleep(1)
                    self.moveforward()
                    time.sleep(0.07)
                    self.stop()
                    time.sleep(1)
                    self.turnleft()
                    time.sleep(0.4)
                    self.stop()
                    time.sleep(1)
                    PWM.set_duty_cycle(self.servo, SG90_LEFT)
                    time.sleep(1)
                    self.turnleft()
                    time.sleep(1.65)
                    self.stop()
                    time.sleep(2)
                    PWM.set_duty_cycle(self.servo, SG90_RIGHT)
                    time.sleep(1)
                    
                    # Draw right eye
                    self.movebackward()
                    time.sleep(0.1)
                    self.stop()
                    time.sleep(1)
                    PWM.set_duty_cycle(self.servo, SG90_LEFT)
                    time.sleep(1)
                    self.movebackward()
                    time.sleep(0.1)
                    self.stop()
                    time.sleep(2)
                    PWM.set_duty_cycle(self.servo, SG90_RIGHT)
                    time.sleep(1)
                    
                    # Draw left eye
                    self.movebackward()
                    time.sleep(0.4)
                    self.stop()
                    time.sleep(1)
                    self.turnleft()
                    time.sleep(0.5)
                    self.stop()
                    time.sleep(1)
                    self.moveforward()
                    time.sleep(0.04)
                    self.stop()
                    time.sleep(1)
                    self.turnright()
                    time.sleep(0.45)
                    self.stop()
                    time.sleep(1)
                    self.movebackward()
                    time.sleep(0.02)
                    self.stop()
                    time.sleep(1)
                    PWM.set_duty_cycle(self.servo, SG90_LEFT)
                    time.sleep(1)
                    self.moveforward()
                    time.sleep(0.16)
                    self.stop()
                    time.sleep(2)
                    PWM.set_duty_cycle(self.servo, SG90_RIGHT)
                    time.sleep(1)
                    
                    # Draw smile
                    if (emotion == "happy"):
                        self.turnright()
                        time.sleep(0.45)
                        self.stop()
                        time.sleep(1)
                        self.moveforward()
                        time.sleep(0.3)
                        self.stop()
                        time.sleep(1)
                        self.turnleft()
                        time.sleep(0.9)
                        self.stop()
                        time.sleep(1)
                        self.moveforward()
                        time.sleep(0.35)
                        self.stop()
                        time.sleep(1)
                        self.turnleft()
                        time.sleep(0.2)
                        self.stop()
                        time.sleep(1)
                        PWM.set_duty_cycle(self.servo, SG90_LEFT)
                        time.sleep(1)
                        self.turnleft()
                        time.sleep(0.3)
                        self.stop()
                        time.sleep(2)
                        PWM.set_duty_cycle(self.servo, SG90_RIGHT)
                        time.sleep(1)
                       
                    # Draw frown
                    if (emotion == "sad"):
                        self.movebackward()
                        time.sleep(0.2)
                        self.stop()
                        time.sleep(1)
                        PWM.set_duty_cycle(self.servo, SG90_LEFT)
                        time.sleep(1)
                        self.turnright()
                        time.sleep(0.3)
                        self.stop()
                        time.sleep(2)
                        PWM.set_duty_cycle(self.servo, SG90_RIGHT)
                        time.sleep(1)
                    
                    # Turn light off
                    GPIO.output(self.blue_led, GPIO.LOW)
    
    # End def
    
    
    def cleanup(self):
        """Cleanup the hardware components."""
        
        # Clean up GPIOs
        GPIO.output(self.yellow_led, GPIO.LOW)
        GPIO.output(self.blue_led, GPIO.LOW)
        
        # Clean up GPIOs
        GPIO.cleanup()
        
        # Stop servo
        PWM.stop(self.servo)
        PWM.cleanup()
        
        # Stop left and right motors
        self.stop()
    
    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    
    # Create instantiation of the robot
    robot = Robot()
    
    try:
        # Run the robot
        robot.run()
    
    except KeyboardInterrupt:
        # Clean up hardware when exiting
        robot.cleanup()
    
    print(" Program Complete")