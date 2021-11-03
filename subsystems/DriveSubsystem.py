import wpilib
import wpilib.drive
from wpilib.drive import MecanumDrive
import commands2
import constants

class DriveSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.frontLeftChannel = 1
        self.rearLeftChannel = 2
        self.frontRightChannel = 3
        self.rearRightChannel = 4

        self.frontLeftMotor = wpilib.Talon(self.frontLeftChannel)
        self.rearLeftMotor = wpilib.Talon(self.rearLeftChannel)
        self.frontRightMotor = wpilib.Talon(self.frontRightChannel)
        self.rearRightMotor = wpilib.Talon(self.rearRightChannel)

        self.leftEncoder = wpilib.Encoder(6, 7)
        self.leftEncoder.setDistancePerPulse(1/20)

        self.gyro = wpilib.AnalogGyro(1)
        
        self.gyro.initGyro()
        self.gyro.setSensitivity(self.gyro.kDefaultVoltsPerDegreePerSecond)  # calibrates gyro values to equal degrees

        self.drive = MecanumDrive(
            self.frontLeftMotor,
            self.rearLeftMotor,
            self.frontRightMotor,
            self.rearRightMotor,
        )
    def mecanumDrive(self, x, y, rot):
        """
        Drives the robot using Mecanum controls.
        """
        self.drive.driveCartesian(x, y, rot, 0)
    
    def resetEncoders(self):
        """Resets the drive encoders to currently read a position of 0."""
        self.leftEncoder.reset()
    
    def resetGyro(self):
        """Resets the gyro to currently read a position of 0."""
        self.gyro.reset()

    def getEncoderDistance(self) -> float:
        """Gets the average distance of the TWO encoders."""
        return self.leftEncoder.getDistance()

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the
        drive to drive more slowly.
        """
        self.drive.setMaxOutput(maxOutput)

    

