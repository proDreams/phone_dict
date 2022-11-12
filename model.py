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
            temp = user_interface.get_row()
            print(temp)
            writer.writerow(temp)
        print(f'Файл db.csv успешно обновлён!')
    except:
        print('Произошла ошибка, попробуйте снова!')


def change_row():
    file = open('db.csv', 'r+', newline='', encoding='utf-8')
    reader = csv.reader(file)
    reader = list(reader)
    id = input('Введите id для поиска: ')
    for i in range(len(reader)):
        temp = ''.join(reader[i]).split(';')
        if temp[0] == id:
            temp = input('Введите новые данные\n').split()
        reader[i] = temp
    file.close()
    file = open('db.csv', 'w+', newline='', encoding='utf-8')
    file.close()
    file = open('db.csv', 'r+', newline='', encoding='utf-8')
    writer = csv.writer(file, delimiter=';')
    for i in reader:
        print(i)
        writer.writerow(i)
    file.close()



def create_csv():
    filename = user_interface.get_filename()
    with open(f'{filename}.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'first_name', 'last_name', 'dob', 'work_place', 'phone_number']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
