import commands2

from subsystems.DriveSubsystem import DriveSubsystem


class DriveDistance(commands2.CommandBase):
    def __init__(self, centimeters: float, speed: float, drive: DriveSubsystem) -> None:
        super().__init__()
        self.distance = centimeters
        self.speed = speed
        self.drive = drive
        self.addRequirements([drive])

    def initialize(self) -> None:
        self.drive.resetOdometry()

    def execute(self) -> None:
        self.drive.arcadeDrive(self.speed, 0)

    def end(self, interrupted: bool) -> None:
        self.drive.arcadeDrive(0, 0)

    def isFinished(self) -> bool:
        return self.drive.getAverageEncoderDistance() >= self.distance