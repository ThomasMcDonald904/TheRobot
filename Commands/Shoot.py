import wpilib
import commands2

from subsystems.ShooterSubsystem import ShooterSubsystem

class Shoot(commands2.CommandBase):
    def __init__(self, shootSub: ShooterSubsystem) -> None:
        super().__init__()
        self.shootSubsystem = shootSub
        self.timer = wpilib.Timer()
        self.addRequirements(self.shootSubsystem)
    
    def initialize(self) -> None:
        self.timer.reset()
        self.timer.start()

    def execute(self):
        self.shootSubsystem.shooterMotor.set(1)

    def end(self, interrupted: bool):
        self.shootSubsystem.shooterMotor.set(1)
        self.timer.stop()

    def isFinished(self) -> bool:
        return self.timer.get() >= 3
