# -*- coding: windows-1251 -*-
"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""


class BankAccount():
    def __init__(self, name, balance, passport):
        self._name = name
        self.__balance = balance
        self.__passport = passport


    def getbalance(self):
        return self.__balance

    def getpassport(self):
        return self.__passport


    def setbalance(self, newbalance):
        if newbalance < 0:
            print("У вас недостаточно средств")
        else:
            print("Вызывли степпер")
            self.__balance = newbalance


    def setnomerpassport(self,password,passport):
        if password == "1234":
            print("Вы в системе")
            self.__passport = passport
        else:
            print("Измените пароль")


    def delpassport(self, password):
        if password == "123456789":
            del self.__passport


account1 = BankAccount("Даник", 1000000, 99999)
print(account1.getbalance())
print(account1.getpassport())
account1.setbalance(-23)
account1.setnomerpassport(5346,25236)
account1.delpassport(2523)