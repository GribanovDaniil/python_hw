"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def cacluate(*numbers):
    counter = 0

    t = ()
    num = []
    for i in numbers:
        counter = counter + i
    formul = counter / len(numbers)

    for i in numbers:
        if i > formul:
            num.append(i)

    t = (formul, num)
    return t

print(cacluate(7,7,5,4,8,9,2,1,3,4,5))