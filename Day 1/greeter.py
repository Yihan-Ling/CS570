
class Greeter:

    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self):
        print(self.greeting)

if __name__ == '__main__':
    x = Greeter('Hello')
    y = Greeter('Konnichiwa')
    x.greet()
    y.greet()
