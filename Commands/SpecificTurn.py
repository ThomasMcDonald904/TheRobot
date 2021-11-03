import commands2

from subsystems.driveSubsystem import DriveSubsystem


class SpecificTurn(commands2.CommandBase):
    def __init__(self, angle: float, drive: DriveSubsystem):
        super().__init__()
        self.angle = angle
        self.drive = drive
        self.addRequirements([drive])

    def initialize(self):
        self.drive.resetGyro()

    def execute(self):
        self.drive.mecanumDrive(0, 0, 1.0)

    def end(self, interrupted: bool):
        self.drive.mecanumDrive(0, 0, 0.0)

    def isFinished(self) -> bool:
        self.drive.gyro.getAngle() >= self.angle