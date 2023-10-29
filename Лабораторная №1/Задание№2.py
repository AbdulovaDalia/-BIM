Volume = 1.44  # Информационный объем дискеты равен
Numbers_of_pages = 100  # Количество страниц в книге
Number_of_lines = 50  # Число строк на странице
Number_of_characters = 25  # Количество символов в строке
One_characters = 4  # Для хранения кода одного символа нужно 4 байта

Volume_b = Volume*1024*1024
Number_of_books = round((Volume_b / (Numbers_of_pages * Number_of_lines * Number_of_characters * One_characters)))

print("Количество книг, помещающихся на дискету:", Number_of_books)
