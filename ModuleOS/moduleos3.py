# -*- coding: windows-1251 -*-
"""�������� ���������-����� ������� ��������������� ����� c ������� �������� � ����� ��������� ����� target,
����� ����� ���������� ��������������.
"""


import os
for i in range(1, 11):
    if i % 2 == 0:
        os.rename('C:\\target\ ' + str(i), 'C:\target\olegpython' + str(i))
