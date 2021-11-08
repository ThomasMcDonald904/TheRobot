import wpilib
import wpilib.simulation
import commands2
from wpilib.drive import DifferentialDrive
from wpimath.geometry import Pose2d, Rotation2d
from wpimath.kinematics import DifferentialDriveOdometry
from wpimath.system.plant import DCMotor


class DriveSubsystem(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.frontLeft = wpilib.PWMVictorSPX(1)
        self.rearLeft = wpilib.PWMVictorSPX(2)
        self.frontRight = wpilib.PWMVictorSPX(3)
        self.rearRight = wpilib.PWMVictorSPX(4)

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(
            wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft),
            wpilib.SpeedControllerGroup(self.frontRight, self.rearRight),
        )

        # The left-side drive encoder
        self.leftEncoder = wpilib.AnalogEncoder(6, 7)

        # The right-side drive encoder
        self.rightEncoder = wpilib.AnalogEncoder(8, 9)
        self.gyro = wpilib.ADXRS450_Gyro()
        # Sets the distance per pulse for the encoders
        self.leftEncoder.setDistancePerRotation(1/20)
        self.rightEncoder.setDistancePerRotation(1/20)

        if wpilib.RobotBase.isSimulation():
            self.field = wpilib.Field2d()
            wpilib.SmartDashboard.putData("Field", self.field)

            self.odometry = DifferentialDriveOdometry(Rotation2d.fromDegrees(0.0))
            self.gyro_sim = wpilib.simulation.ADXRS450_GyroSim(self.gyro)
            self.leftEncoder = wpilib.simulation.EncoderSim(self.leftEncoder)
            self.rightEncoder = wpilib.simulation.EncoderSim(self.rightEncoder)
            self.drive_sim = wpilib.simulation.DifferentialDrivetrainSim(
                DCMotor.NEO(2),  # 2 NEO motors on each side of the drivetrain
                7.29,  # 7.29:1 gearing reduction
                7.5,  # MOI of 7.5 kg m^2 (from CAD model)
                60.0,  # The mass of the robot is 60 kg
                0.08,  # The robot uses 8cm radius wheels
                0.71,  # The track width is 0.71 meters
                # The standard deviations for measurement noise:
                # x and y:          0.001 m
                # heading:          0.001 rad
                # l and r velocity: 0.1   m/s
                # l and r position: 0.005 m
                [0.001, 0.001, 0.001, 0.1, 0.1, 0.005, 0.005]
            )

    def simulationPeriodic(self) -> None:
        input_voltage = wpilib.RobotController.getBatteryVoltage()
        self.drive_sim.setInputs(
            self.frontLeft.get() * input_voltage,
            -1.0 * self.frontRight.get() * input_voltage
        )

        self.drive_sim.update(0.02)  # 20 ms, e.g. 50 updates/sec

        # Update sensors
        self.leftEncoder.setDistance(self.drive_sim.getLeftPosition())
        self.leftEncoder.setRate(self.drive_sim.getLeftVelocity())
        self.rightEncoder.setDistance(self.drive_sim.getRightPosition())
        self.rightEncoder.setRate(self.drive_sim.getRightVelocity())
        self.gyro_sim.setAngle(-1.0 * self.drive_sim.getHeading().degrees())

        # Update odometry
        self.odometry.update(
            Rotation2d.fromDegrees(self.getAngle()),
            self.leftEncoder.getDistance(),
            self.rightEncoder.getDistance(),
        )
        self.field.setRobotPose(self.odometry.getPose())

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        """
        Drives the robot using arcade controls.
        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        self.drive.arcadeDrive(fwd, rot)

    def resetEncoders(self) -> None:
        """Resets the drive encoders to currently read a position of 0."""
        self.gyro.reset()

    def getAverageEncoderDistance(self) -> float:
        """Gets the average distance of the TWO encoders."""
        return (self.leftEncoder.getDistance() + self.rightEncoder.getDistance()) / 2.0

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the
        drive to drive more slowly.
        """
        self.drive.setMaxOutput(maxOutput)