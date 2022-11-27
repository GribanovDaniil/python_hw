# -*- coding: windows-1251 -*-
"""
Класс Vector3D
Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
Обязательно должны быть реализованы методы:
– приведение вектора к строке с выводом кооржинат (метод __str __),
– сложение векторов оператором `+` (метод __add__),
– вычитание векторов оператором `-` (метод __sub__),
– скалярное произведение оператором `*` (метод __mul__),
"""
class Vector3D():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod

    def __add__(self, other):
        return (self.x + other, self.y + other, self.z + other)


    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)


    def __sub__(self, other):
        return (self.x - other, self.y - other,self.z - other)


V1 = Vector3D(11,12,3)