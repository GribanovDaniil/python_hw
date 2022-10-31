list1 = [1,2,3,4,5,6]
list2 = [4,16,1,3,8,2]

matching_numbers = []

for i in list1:
    if i in list2:
        matching_numbers.append(i)

matching_numbers.sort()

print(matching_numbers)