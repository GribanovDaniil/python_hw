full_name = input("Введите ФИО: ")
post = input('Введите должность: ')
quantity_students = input("Введите количетсво студентов: ").split(',')

prepod_info = []

prepod_info.append(full_name)
prepod_info.append(post)
prepod_info.append(quantity_students)

common = []

common.append(prepod_info)

print(common)