"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""

# def show_letters(str):
#     yield from ''.join([letter for letter in str if letter.isalpha()]) #
#
#
# random_str = show_letters('A!sdf 09 _ w')
# print(next(random_str))
# print(next(random_str))

def show_letters(str):
    for i in str:
        if i.isalpha():
            yield i


def main():
    a = show_letters('6e2678gr''27gsuy@11bcdj/;]')
    for el in a:
        print(el)

main()