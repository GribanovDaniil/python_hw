"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""
example_dict = {number: number ** 3 for number in range(1, 11)}
print(example_dict)