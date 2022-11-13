import csv
import user_interface


def view_row(file_name):
    user_interface.view_file('db.csv')
    with open(f'{file_name}.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            user_interface.print_output(i)


def create_row(file_name):
    try:
        with open(f'{file_name}.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            temp = user_interface.get_row()
            print(temp)
            writer.writerow(temp)
        print(f'Файл db.csv успешно обновлён!')
    except:
        print('Произошла ошибка, попробуйте снова!')


def change_row(file_name):
    file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    reader = csv.reader(file)
    reader = list(reader)
    record_id = user_interface.get_id()
    for i in range(len(reader)):
        temp = ''.join(reader[i]).split(';')
        if temp[0] == record_id:
            user_interface.print_found_id(temp, reader[0])
            temp = user_interface.get_new_data()
        reader[i] = temp
    file.close()
    file = open(f'{file_name}.csv', 'w+', newline='', encoding='utf-8')
    file.close()
    file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    writer = csv.writer(file, delimiter=';')
    for i in reader:
        writer.writerow(i)
    file.close()


def create_csv():
    filename = user_interface.get_filename()
    with open(f'{filename}.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'first_name', 'last_name', 'dob', 'work_place', 'phone_number']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()


def check_file_exist(file_name):
    try:
        file = open(f'{file_name}.csv', 'r', newline='', encoding='utf-8')
        file.close()
        return True
    except:
        user_interface.check_file_error()
        return False
