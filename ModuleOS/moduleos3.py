# -*- coding: windows-1251 -*-
"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""


import os
for i in range(1, 11):
    if i % 2 == 0:
        os.rename('C:\\target\ ' + str(i), 'C:\target\olegpython' + str(i))
