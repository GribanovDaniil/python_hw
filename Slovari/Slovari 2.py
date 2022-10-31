"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"

dct = {number: numbers.count(number) for number in numbers}
print(dct)

example = {}
for number in numbers:
    example[number] = numbers.count(number)

print(example)