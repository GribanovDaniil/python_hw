"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def imt(weight, height):
    index = weight / (height * height)
    return index

index = imt(int(input()), int(input()))
def counter():
    if index < 18.5:
        print("Недостаточный вес.")
    if 18.5 <= index <= 25:
        print("ИМТ в норме.")
    if index > 25:
        print("Избыточный вес.")

counter()