# -*- coding: windows-1251 -*-
"""
�������� ��������� ��������� ����� target ������ ������� ��� 10 ����� ����� ������� ����� �� 1 �� 10
"""


import os

os.mkdir(r'C:\\target')
for i in range(1, 11):
    os.mkdir('C:\\target\ ' + str(i))
