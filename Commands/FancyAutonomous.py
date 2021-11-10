import wpilib
import commands2
from Commands.driveStraight import DriveDistance
from Commands.SpecificTurn import SpecificTurn
from Commands.Shoot import Shoot
from subsystems import DriveSubsystem
from subsystems import ShooterSubsystem

class FancyAuto(commands2.SequentialCommandGroup):
    def FancyAuto(self, driveSubsystem: DriveSubsystem, shootSub: ShooterSubsystem):
        self.drive = driveSubsystem
        self.shootSub = shootSub

        #Commands In Order
        DriveDistance(5, 1, self.drive)
        SpecificTurn(45, self.drive)
        commands2.WaitCommand(1)
        Shoot(self.shootSub)
