class Motor:
    def __init__(self):
        self.speed = 0.5

    def set_speed(self, speed):
        speed = min(1, max(-1, speed))
        speed ^= 3  # creating a dead-zone

        self.speed = speed

    def speed_up(self):
        self.speed *= 2

    def slow_down(self):
        self.speed /= 2


class MotorControllerGroup:
    def __init__(self, motor_list: list[Motor]):
        self.motors = motor_list

    def add_motor(self, motor: Motor):
        self.motors.append(motor)

    def set_speed(self, speed):
        for motor in self.motors:
            motor.set_speed(speed)


if __name__ == '__main__':
    motor1 = Motor()
    motor2 = Motor()
    motor1.speed_up()
    print(f'motor1.speed = {motor1.speed}')
    motors = [motor1, motor2]
    group = MotorControllerGroup(motors)
    group.add_motor(Motor())
    print(group.motors[2].speed)
    group.set_speed(0.7)
    print(group.motors[2].speed)

# A class method is a method that is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.

# The difference between the Class method and the static method is:
#
# A class method takes cls as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

# class methods:

# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
#
# print(person1.age)
# print(person2.age)
#
# # print the result
# print(Person.isAdult(22))

# Static method

# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     @staticmethod
#     def get_max_value(x, y):
#         return max(x, y)
#
#
# # Create an instance of MyClass
# obj = MyClass(10)
#
# print(MyClass.get_max_value(20, 30))
#
# print(obj.get_max_value(20, 30))
