from settings import *
import csv
import random


def view_row(file_name):
    user_interface.view_file('db.csv')
    with open(f'{file_name}.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            user_interface.print_output(i)
    controller.menu()


def create_row(file_name):
    with open(f'{file_name}.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        temp = user_interface.get_row()
        user_interface.show_add_row(temp)
        writer.writerow(temp)
    user_interface.add_row_success(file_name)
    controller.menu()


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
            while len(temp) != 6:
                user_interface.get_new_data()
        reader[i] = temp
    file.close()
    file = open(f'{file_name}.csv', 'w+', newline='', encoding='utf-8')
    file.close()
    file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    writer = csv.writer(file, delimiter=';')
    for i in reader:
        writer.writerow(i)
    file.close()
    controller.menu()


def delete_row(file_name):
    file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    reader = csv.reader(file)
    reader = list(reader)
    record_id = user_interface.get_delete_id()
    for i in range(len(reader)):
        temp = ''.join(reader[i]).split(';')
        if temp[0] == record_id:
            del reader[i]
            break
    file.close()
    file = open(f'{file_name}.csv', 'w+', newline='', encoding='utf-8')
    file.close()
    file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    writer = csv.writer(file, delimiter=';')
    for i in reader:
        writer.writerow(i)
    file.close()
    controller.menu()


def create_csv():
    filename = user_interface.get_filename()
    with open(f'{filename}.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'first_name', 'last_name', 'birth_date', 'work_place', 'phone_number']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
    controller.menu()


def check_file_exist(file_name):
    try:
        file = open(f'{file_name}.csv', 'r', newline='', encoding='utf-8')
        file.close()
        return True
    except:
        user_interface.check_file_error()
        return False


def generate_phone_book(file_name):
    generated_list = generate_list()
    with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8') as file:
        field_names = ['id', 'first_name', 'last_name', 'birth_date', 'work_place', 'phone_number']
        writer = csv.DictWriter(file, fieldnames=field_names, delimiter=';')
        writer.writeheader()
        writer = csv.writer(file, delimiter=';')
        writer.writerows(generated_list)
    user_interface.generate_book_success(file_name)
    controller.menu()


def generate_list():
    how_many = user_interface.quantity_records()
    text = [chr(i) for i in range(65, 123) if chr(i).isalpha()]
    digits = [str(i) for i in range(10)]
    generated_list = []
    for i in range(1, how_many + 1):
        generated_list.append([i, ''.join(random.sample(text, random.randint(5, 8))),  # Имя
                               ''.join(random.sample(text, random.randint(5, 8))),  # Фамилия
                               f'{random.randint(1, 30)}.{random.randint(1, 12)}.{random.randint(1990, 2008)}',
                               # Дата рождения
                               ''.join(random.sample(text, random.randint(7, 12))),  # Место работы
                               f'+7{"".join(random.sample(digits, 10))}'])  # Номер телефона)
    return generated_list
