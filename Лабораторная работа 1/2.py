# TODO Найдите количество книг, которое можно разместить на дискете
Total = 1.44 * 1024 * 1024
One_book = 25 * 50 * 100 * 4
Book_on_disk = int(Total//One_book)
print("Количество книг, помещающихся на дискету:", Book_on_disk)
