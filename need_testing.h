#include "vex.h"

using namespace vex;

// Create the brain and PWM output on 3-wire port A
brain  Brain;
pwm_out servoA(Brain.ThreeWirePort.A);

int main() {
  // Let system start up
  wait(1, seconds);
  Brain.Screen.print("Starting servo sweep...");

  while (true) {
    // Move to far left (approximately 0°)
    servoA.setState(-100, percentUnits::pct);  // ~1ms pulse
    Brain.Screen.clearLine();
    Brain.Screen.print("Position: Left (-100%%)");
    wait(1000, msec);

    // Move to center (approximately 90°)
    servoA.setState(0, percentUnits::pct);     // ~1.5ms pulse
    Brain.Screen.clearLine();
    Brain.Screen.print("Position: Center (0%%)");
    wait(1000, msec);

    // Move to far right (approximately 180°)
    servoA.setState(100, percentUnits::pct);   // ~2ms pulse
    Brain.Screen.clearLine();
    Brain.Screen.print("Position: Right (100%%)");
    wait(1000, msec);
  }
}
