def mode_choice():
    print('''Choose a mode:
    1 - Создать файл
    2 - Просмотр файла
    3 - Добавить информацию
    4 - Изменить строку
    5 - Удалить строку
    6 - Сгенерировать справочник
    0 - Вернуться к выбору файла
    X - Quit''')
    return input(': ').lower()


def choice_file_prints():
    return input('- Введите название файла или путь к файлу с данными\n'
                 '- Наберите "new_file" для создания нового\n'
                 '- Или нажмите "Enter" для файла по умолчанию.\n')


def check_file_error():
    print('Ошибка открытия файла или пути к файлу\n'
          'Попробуйте снова.')


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


def get_delete_id():
    return input('Введите id для удаления: ')


def get_new_data():
    return input('Введите новые данные:\n').split()


def print_found_id(row, cols):
    print('Найдена строка:')
    print(*row)


def quantity_records():
    return int(input('Введите количество записей для генерации: '))


def show_add_row(row):
    print(f'Добавлена строка:'
          f'{row}')


def add_row_success(file):
    print(f'Файл {file}.csv успешно обновлён!')

def generate_book_success(file):
    print(f'Файл {file} успешно сгенерирован!')

def exit_program():
    print('Выход из программы.')

def menu_error():
    print('Wrong choice. Try again!')

def new_line()
    print()