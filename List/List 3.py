marks = input("Введите оценки: ").split()

mark_not_five = 0
counter_of_five = 0

for i in marks:
    if i == '5':
        counter_of_five += 1

print('процент пятерок',(counter_of_five / len(marks)) * 100)