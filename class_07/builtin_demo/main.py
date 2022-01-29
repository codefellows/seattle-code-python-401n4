import builtins

_print = builtins.print
_input = builtins.input

def alter():
    builtins.print = _input
    builtins.input = _print

def alter_back():
    builtins.print = _print
    builtins.input = _input


if __name__ == '__main__':
    alter()
    print('Hello There!')
    input('What is your name > ')

    alter_back()
    print('Hello There!')
    input('What is your name > ')