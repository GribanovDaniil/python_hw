# -*- coding: windows-1251 -*-
"""
�������� ����� ������� ����� ������������� �������� name � ����� �����
������� � ����� ���������� ������� "�����". �������� ��� 1 �����, ����������� ����������.
�� ������ ������ �������� ����� ������ �������� � �������� � ������ ������� "�� ��� �������� ���� �� �� ����� ����� ���".
�������� ��������� ������� ������ � ����� ������ � �������� ����� ���������� ��� �������.
"""


class Fullname:

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"{self.name} �����")


class Name(Fullname):

    def display_info_dop(self):
        print(f"{self.name} ����� � ��� �� ��������")

nastya = Fullname("�����")
nastya.display_info()

nastya = Name("�����")
nastya.display_info_dop()