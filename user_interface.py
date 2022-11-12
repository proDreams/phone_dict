def user_choice():
    print('''Choose a number:
    1 - Создать файл
    2 - Просмотр файла
    3 - Добавить информацию
    X - Quit''')
    choice = input(': ')
    return choice


def print_output(row):
    print(row)
