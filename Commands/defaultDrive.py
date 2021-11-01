import commands2
# import Subsystems
from subsystems import DriveSubsystem


class DefaultDrive(commands2.CommandBase):
    def __init__(self, drive: DriveSubsystem) -> None:
        super().__init__()
        self.drive = drive

        self.addRequirements([self.drive])

    def execute(self, x, y, rot) -> None:
        self.drive.MecanumDrive(x, y, rot)
