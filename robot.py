from colorama.ansi import Style
import commands2
from commands2 import button
import wpilib
from wpilib._wpilib import Joystick, Solenoid, wait
from wpilib.drive import MecanumDrive
from colorama import Fore
import constants

from Commands.defaultDrive import DefaultDrive
from subsystems.driveSubsystem import DriveSubsystem

class MyRobot(commands2.TimedCommandRobot):
    """Main robot class"""
 
    # The channel on the driver station that the joystick is connected to

    def robotInit(self):
        """Robot initialization function"""

        self.ballThrower = wpilib.Spark(8)
        self.lStickChannel = 0
 
        # Position gets automatically updated as robot moves
        self.leftEncoder = wpilib.Encoder(6, 7)
        self.rightEncoder = wpilib.Encoder(8, 9)
        
        self.rightEncoder.setDistancePerPulse(1/40)
        self.leftEncoder.setDistancePerPulse(1/40)

        self.lstick = Joystick(self.lStickChannel)
        self.driveSubsystem = DriveSubsystem()
        self.driveSubsystem.setDefaultCommand(DefaultDrive(self.driveSubsystem, self.lstick))

        
 
    def disabled(self):
        """Called when the robot is disabled"""
        while self.isDisabled():
            wpilib.Timer.delay(0.01)
 
    def autonomousInit(self):
        """Called when autonomous mode is enabled"""
 
    def autonomousPeriodic(self):
       pass
 
       
 
    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""
 
 
if __name__ == "__main__":
    wpilib.run(MyRobot)