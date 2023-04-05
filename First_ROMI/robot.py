import wpilib
from wpilib import TimedRobot, Joystick, Spark
from wpilib.drive import DifferentialDrive
import os


class MyRobot(TimedRobot):
    def robotInit(self):
        # This method is called as the robot turns on and is often used to setup the joysticks and other presets.
        self.controller = Joystick(0)
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

    def robotPeriodic(self):
        # This is called every cycle of the code. In general the code is loop through every .02 seconds.
        pass

    def autonomousInit(self):
        # This is called once when the robot enters autonomous mode.
        pass

    def autonomousPeriodic(self):
        # This is called every cycle while the robot is in autonomous.
        pass

    def teleopInit(self):
        # This is called once at the start of Teleop.
        pass

    def teleopPeriodic(self):
        # This is called once every cycle during Teleop
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward, rotate)


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
