# -*- coding: windows-1251 -*-
""" �������� ��������� ������� ������� ����� task4 � ���������� ����� "� �������� �������" � ���� answer.txt
"""


import os
os.mkdir(r'C:\task4')
os.chdir(r'C:\task4')
with open('answer.txt', 'w') as f:
    f.write('� �������� ������� ')
