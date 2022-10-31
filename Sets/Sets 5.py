students = int(input("Введите количество студентов:"))
lst = []
while students != 0:
       ask = int(input("Сколько студентов знают языки:"))
       for i in range(ask):
              ask1 = input("Какие языки Вы знаете:")
              lst.append(ask1)
       students -= ask

       print(len(lst), "-", lst)
       lst = []