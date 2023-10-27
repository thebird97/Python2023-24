class Snake:
    pass


class Python(Snake):
    pass


print(Python.__name__, 'is a', Snake.__name__)

print(Python.__bases__[0].__name__, 'can be', Python.__name__)