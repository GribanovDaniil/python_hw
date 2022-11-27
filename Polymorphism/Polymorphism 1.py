# -*- coding: windows-1251 -*-
"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class People():
    def quack(self):
        print("Я имитирую кряк-кряк")


    def clothes(self):
        print("Я ношу одежду")


class Duck(People):
    def quack(self):
        print("Я крякаю")


    def clothes(self):
        print("Я ношу анашу")

a = People()
b = Duck()
ab = [a, b]
for i in ab:
    i.quack()
    i.clothes()