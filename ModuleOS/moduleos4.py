# -*- coding: windows-1251 -*-
""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""


import os
os.mkdir(r'C:\task4')
os.chdir(r'C:\task4')
with open('answer.txt', 'w') as f:
    f.write('я выполнил задание ')
