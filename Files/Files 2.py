"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open("python2.txt", "w") as f:
    f.write(", но у меня не получается.")

with open("python.txt", "r") as f:
    text = f.read()

with open("python2.txt", "r") as f:
    text1 = f.read()

print(text + text1)