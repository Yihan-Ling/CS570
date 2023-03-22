from greeter import Greeter

def print_hi(name):
    print(f'Hi, {name}')
    # a procedure, not a function because it doesn't have a return


if __name__ == '__main__':
    print_hi('Carson')
    x = Greeter('Hi')
    x.greet()
