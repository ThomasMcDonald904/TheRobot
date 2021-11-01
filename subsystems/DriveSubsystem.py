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
        self.lStickChannel = 0
        self.rStickChannel = 1

        self.frontLeftMotor = wpilib.Talon(self.frontLeftChannel)
        self.rearLeftMotor = wpilib.Talon(self.rearLeftChannel)
        self.frontRightMotor = wpilib.Talon(self.frontRightChannel)
        self.rearRightMotor = wpilib.Talon(self.rearRightChannel)


        self.gyro = wpilib.AnalogGyro(1)
        self.leftEncoder = wpilib.Encoder(6, 7)
        self.rightEncoder = wpilib.Encoder(8, 9)
        
        self.gyro.initGyro()
        self.gyro.setSensitivity(self.gyro.kDefaultVoltsPerDegreePerSecond)  # calibrates gyro values to equal degrees
        self.rightEncoder.setDistancePerPulse(constants.kEncoderDistancePerPulse)
        self.leftEncoder.setDistancePerPulse(constants.kEncoderDistancePerPulse)

        self.drive = MecanumDrive(
            self.frontLeftMotor,
            self.rearLeftMotor,
            self.frontRightMotor,
            self.rearRightMotor,
        )
    def MecanumDrive(self, x, y, rot) -> None:
        """
        Drives the robot using Mecanum controls.
        """
        self.drive.driveCartesian(x, y, rot, 0)
    
    def resetEncoders(self) -> None:
        """Resets the drive encoders to currently read a position of 0."""
    
    def getAverageEncoderDistance(self) -> float:
        """Gets the average distance of the TWO encoders."""
        return (self.leftEncoder.getDistance() + self.rightEncoder.getDistance()) / 2.0

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the
        drive to drive more slowly.
        """
        self.drive.setMaxOutput(maxOutput)

    

