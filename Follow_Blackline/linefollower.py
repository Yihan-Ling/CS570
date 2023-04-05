from wpilib import DigitalInput


class LineFollower():
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        self.left_input = DigitalInput(8)
        self.right_input = DigitalInput(9)

    def run(self):
        if self.left_input.get():
            self.drivetrain.drive(0.3, -0.3)
        elif self.left_input.get():
            self.drivetrain.drive(0.3, 0.3)
        else:
            self.drivetrain.drive(0.3, 0)

