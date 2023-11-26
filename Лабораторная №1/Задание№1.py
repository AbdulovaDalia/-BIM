numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_list = numbers[0:4]
new_list_1 = numbers[5:]

correct_number = (sum(new_list) + sum(new_list_1)) / len(numbers)
incorrect_number = numbers[4]
numbers[4] = correct_number

print("Измененный список:", numbers)