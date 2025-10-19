# VEX Robotics Practice Suite

## Overview
This repository gathers small VEX programs that help test servo control and tank driving. Each script is ready to load through VEXcode and can be adjusted for classroom or workshop practice.

## File Guide
* `version1.py` lets the controller buttons move a servo to stored angles and returns it to center when the button is released.
* `version2.py` provides a steady tank drive loop that mixes the vertical and horizontal joystick axes to command two drive motors.
* `need_testing.h` shows a compact C plus plus example that sweeps a servo across left center and right positions while printing status on the brain screen.

## Getting Started
1. Open VEXcode in Python or C plus plus mode as needed.
2. Create a new project and match the device setup to the ports shown in the script you plan to run.
3. Copy the desired file contents into the project main file.
4. Build and download to the brain, then test the behavior with the handheld controller.

## Keeping This Guide Current
Review this document whenever you push commits or edit the code. Update the descriptions above so that they match the latest behavior. Add any setup tips that future drivers or builders should know after new testing sessions.

## Support Notes
* Use the VEX device info view to confirm motor and servo ports before running code.
* If you change controller bindings record the new button map inside the related file for clarity.
* Share feedback from drivers after each practice so the code stays responsive.
