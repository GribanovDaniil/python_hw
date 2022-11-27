# -*- coding: windows-1251 -*-
class Add():
    def __init__(self, argument):
        self.argument = argument

    def __add__(self, other):
        return other + self.argument
z = Add(355)
x = Add(99)
t = z + x
print(t)