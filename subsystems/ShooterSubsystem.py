import wpilib
import commands2

class ShooterSubsystem(commands2.CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.setName("Shooter Base")
        self.shooterMotor = wpilib.PWMTalonSRX(5)

    def shoot(self):
        self.shooterMotor.set(1)

    def stopShooting(self):
        self.shooterMotor.set(0)