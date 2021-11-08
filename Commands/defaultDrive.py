import commands2
from wpilib._wpilib import Joystick
# import Subsystems
from subsystems.DriveSubsystem import DriveSubsystem


class DefaultDrive(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem, lstick: Joystick) -> None:
        super().__init__()
        self.drive = drive
        self.lstick = lstick
        self.addRequirements([self.drive])

    def execute(self) -> None:
        self.drive.arcadeDrive(self.lstick.getX(), self.lstick.getRawAxis(2))
