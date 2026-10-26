def zero(func=None):
    if func == None:
        return 0
    return func(0)

def one(func=None):
    if func == None:
        return 1
    return func(1)

def two(func=None):
    if func == None:
        return 2
    return func(2)

def three(func=None):
    if func == None:
        return 3
    return func(3)

def four(func=None):
    if func == None:
        return 4
    return func(4)

def five(func=None):
    if func == None:
        return 5
    return func(5)

def six(func=None):
    if func == None:
        return 6
    return func(6)

def seven(func=None):
    if func == None:
        return 7
    return func(7)

def eigth(func=None):
    if func == None:
        return 8
    return func(8)

def nine(func=None):
    if func == None:
        return 9
    return func(9)

def plus(a):
    return lambda b: b + a

def minus(a):
    return lambda b: b - a

def times(a):
    return lambda b: b * a

def divided_by(a):
    return lambda b: b // a

print(four(plus(nine())))