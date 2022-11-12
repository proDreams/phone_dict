def user_choice():
    print('''Choose a number:
    1 - Создать файл
    2 - Просмотр файла
    3 - Добавить информацию
    4 - Изменить строку
    X - Quit''')
    choice = input(': ')
    return choice


def print_output(row):
    print(row)
