good_marks = [3, 4, 5]
marks = [5, 3, 2, 4, 3, 3]
marks_length = len(marks)

list_of_quantity_marks = []

list_of_quantity_marks.append(marks.count(3))
list_of_quantity_marks.append(marks.count(4))
list_of_quantity_marks.append(marks.count(5))

counter = 0

for i in list_of_quantity_marks:
    counter = counter + i

progress = (counter/marks_length)*100

print(marks, 'Все оценки')
print(list_of_quantity_marks, 'Список количетсва оценок')
print(progress, 'Успеваемость')
