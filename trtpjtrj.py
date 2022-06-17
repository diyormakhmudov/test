# products_lists = []
# while True:
#     command = input(
#         'Введите команду\n\tadd: Добавить продукт в список\n\tdelete: Удалить продукт из списка'
#         '\n\tshow: Вывод списка продуктов\n\tsearch: Найти продукт из списка\n\tclear: Очистить список\n\tstop: Завершить процесс \nВаша команда:').lower()
#     if command == 'add':
#         product_name = input ('Введите название продукта: ')
#         products_lists.append(product_name)
#     elif command == 'delete':
#         product_name = input('Введите название продукта: ')
#         if product_name not in products_lists:
#             print('Братан будь внимателен там нету такого ')
#         products_lists.remove(product_name)
#     elif command == 'show':
#         print(products_lists)
#     elif command == 'search':
#         product_name = input('Введите название продукта: ')
#         products_lists.index(product_name)
#     elif command == 'clear':
#         product_name = input('Введите название продукта: ')
#         products_lists.clear(product_name)
#     elif command == 'stop':
#         break
#     else:
#         print('братан такой команды нет\n')

# for i in range(1, 10):
#     for num in range(i):
#         print(num, end=" ")