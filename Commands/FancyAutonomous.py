import wpilib
import commands2
from Commands.driveStraight import DriveDistance
from Commands.SpecificTurn import SpecificTurn
from Commands.Shoot import Shoot
from subsystems import DriveSubsystem
from subsystems import ShooterSubsystem

class FancyAuto(commands2.SequentialCommandGroup):
    def __init__(self, drive: DriveSubsystem, shoot: ShooterSubsystem): 
        super().__init__()

        self.addCommands(
            DriveDistance(5, 1, drive),
            SpecificTurn(45, drive),
            Shoot(shoot),
            SpecificTurn(135, drive),
            DriveDistance(5, 1, drive)
        )
