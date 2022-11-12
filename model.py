import csv
import user_interface


def view_row():
    user_interface.view_file('db.csv')
    with open('db.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            user_interface.print_output(i)


def create_row():
    try:
        with open(f'db.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(user_interface.get_row())
        print(f'Файл db.csv успешно обновлён!')
    except:
        print('Произошла ошибка, попробуйте снова!')


def change_row():
    with open('db.csv', 'r', newline='', encoding='utf-8') as file:
        pass


def create_csv():
    return 0
