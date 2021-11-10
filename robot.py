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
from subsystems.DriveSubsystem import DriveSubsystem
from Commands.FancyAutonomous import FancyAuto

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
        SmartDashboard.putData("Drive Distance 10cm", DriveDistance(10, 1, self.driveSubsystem))
        SmartDashboard.putData("SpecificTurn 90", SpecificTurn(90, self.driveSubsystem))
        SmartDashboard.putData("SpecificTurn 180", SpecificTurn(180, self.driveSubsystem))
        SmartDashboard.putData("Fancy Auto", FancyAuto())
        

        
 
    def disabled(self):
        """Called when the robot is disabled"""
        while self.isDisabled():
            wpilib.Timer.delay(0.01)
 
    def autonomousInit(self):
        """Called when autonomous mode is enabled"""
 
    def autonomousPeriodic(self):
        pass

    def teleopInit(self) -> None:
        pass
    
    def teleopPeriodic(self):
        """Called when operation control mode is enabled"""
 
 
if __name__ == "__main__":
    wpilib.run(MyRobot)