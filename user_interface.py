def user_choice():
    print('''Choose a number:
    1 - Создать файл
    2 - Просмотр файла
    3 - Добавить информацию
    4 - Изменить строку
    X - Quit''')
    choice = input(': ').lower()
    return choice


def print_output(row):
    print(row)


def get_row():
    return input('Введите необходимые поля через пробел: ').split()


def view_file(name):
    print(f'Просмотр файла {name}')


def get_filename():
    return input('Введите название создаваемого файла:\n')


def get_id():
    return input('Введите id для поиска: ')


def get_new_data():
    return input('Введите новые данные:\n').split()


def print_found_id(row, cols):
    print('Найдена строка:')
    print(*row)
