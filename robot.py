from colorama.ansi import Style
import commands2
from networktables import NetworkTables
from commands2 import button
import networktables
import wpilib
from wpilib._wpilib import Joystick, SmartDashboard, Solenoid, wait
from wpilib.drive import MecanumDrive
from colorama import Fore
import constants

from Commands.defaultDrive import DefaultDrive
from Commands.driveStraight import DriveDistance
from Commands.SpecificTurn import SpecificTurn
from subsystems.driveSubsystem import DriveSubsystem

class MyRobot(commands2.TimedCommandRobot):
    """Main robot class"""
 
    # The channel on the driver station that the joystick is connected to

    def robotInit(self):
        """Robot initialization function"""

        self.ballThrower = wpilib.Spark(8)
        self.lStickChannel = 0
        # Position gets automatically updated as robot moves

        self.lstick = Joystick(self.lStickChannel)
        self.driveSubsystem = DriveSubsystem()
        self.driveSubsystem.setDefaultCommand(DefaultDrive(self.driveSubsystem, self.lstick))

        # wpilib._wpilib.Sendable.__init__(commands2.CommandScheduler.getInstance())
        # wpilib._wpilib.ErrorBase.__init__(commands2.CommandScheduler.getInstance())
        # wpilib._wpilib.ErrorBase
        
        self.auto_command = SpecificTurn(45.0, self.driveSubsystem)
        

        
 
    def disabled(self):
        """Called when the robot is disabled"""
        while self.isDisabled():
            wpilib.Timer.delay(0.01)
 
    def autonomousInit(self):
        """Called when autonomous mode is enabled"""
        self.auto_command.schedule()
 
    def autonomousPeriodic(self):
        pass

    def teleopInit(self) -> None:
        if(self.auto_command):
            self.auto_command.cancel()
 
    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""
 
 
if __name__ == "__main__":
    wpilib.run(MyRobot)