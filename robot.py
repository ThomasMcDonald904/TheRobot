from colorama.ansi import Style
import wpilib
from wpilib._wpilib import Joystick, wait
from wpilib.drive import MecanumDrive
from colorama import Fore

from Commands import defaultDrive

class MyRobot(wpilib.TimedRobot):
    """Main robot class"""
 
    # The channel on the driver station that the joystick is connected to

    lstick = Joystick(0)
 
    def robotInit(self):
        """Robot initialization function"""

        self.ballThrower = wpilib.Spark(8)
        self.lStickChannel = 0
 
        # Position gets automatically updated as robot moves
        self.solenoid = wpilib.DoubleSolenoid(5)

        self.lstick = Joystick(self.lStickChannel)
        
 
    def disabled(self):
        """Called when the robot is disabled"""
        while self.isDisabled():
            wpilib.Timer.delay(0.01)
 
    def autonomousInit(self):
        """Called when autonomous mode is enabled"""
        self.encoder.setDistancePerPulse(20)
       
        self.timer = wpilib.Timer()
        self.timer.start()
 
    def autonomousPeriodic(self):
       pass
 
       
 
    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""
        defaultDrive.DefaultDrive.execute(self.lstick.getX(), -self.lstick.getY(), self.lstick.getRawAxis(2))
        # self.drive.driveCartesian(
        #     self.lstick.getX(), -self.lstick.getY(), self.rstick.getX(), 0
        # )
        print(self.encoder.getDistance())
        if(self.lstick.getTrigger() == True):
            self.solenoid.set(True)
        else:
            self.solenoid.set(False)
 
 
if __name__ == "__main__":
    wpilib.run(MyRobot)