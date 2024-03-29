"""
Основной функционал программы
"""
from settings import *
import csv
import random


def view_row(file_name):
    """
    Показывает содержимое файла
    """
    user_interface.view_file(f'{file_name}.csv')
    with open(f'{file_name}.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            print_row(i)


def print_row(row):
    """
    Красивый вывод строки
    """
    for i in row:
        for j in i.split():
            if len(j) < 4:
                user_interface.print_output(j.ljust(5))
            else:
                user_interface.print_output(j.ljust(15))
        user_interface.new_line()


def create_row(file_name):
    """
    Добавляет запись в файл
    """
    with open(f'{file_name}.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=' ')
        temp = user_interface.get_row()
        user_interface.show_add_row(temp)
        writer.writerow(temp)
    user_interface.add_row_success(file_name)


def change_row(file_name):
    """
    Изменяет запись в файле

    Находим запись по первому столбцу(id)
    Меняем запись на необходимую
    При количестве элементов сверх количества столбцов, считаем,
    что это дополнительные номера телефонов и добавляем соответствующие столбцы.
    После этого заново перезаписываем файл
    """
    file = open(f'{file_name}.csv', 'r', newline='', encoding='utf-8')
    reader = list(csv.reader(file))
    record_id = user_interface.get_id()
    new_file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    writer = csv.writer(new_file, delimiter=' ')
    for i in range(len(reader)):
        temp = ''.join(reader[i]).split(' ')
        if temp[0] == record_id:
            user_interface.print_found_id(temp)
            temp = user_interface.get_new_data()
            while len(temp) < 6:
                temp = user_interface.get_new_data()
            if len(temp) >= 6:
                for j in range(1, len(temp) - 5):
                    if len(reader[0]) < 6 + j:
                        reader[0].append(f'Add_num_{j}')
        reader[i] = temp
        writer.writerow(reader[i])
    file.close()
    new_file.close()


def delete_row(file_name):
    """
    Изменяет запись в файле

    Находим запись по первому столбцу(id)
    Удаляем строку
    После этого заново перезаписываем файл
    """
    file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    reader = csv.reader(file)
    reader = list(reader)
    record_id = user_interface.get_delete_id()
    for i in range(len(reader)):
        temp = ''.join(reader[i]).split(' ')
        if temp[0] == record_id:
            del reader[i]
            break
    file.close()
    file = open(f'{file_name}.csv', 'w+', newline='', encoding='utf-8')
    file.close()
    file = open(f'{file_name}.csv', 'r+', newline='', encoding='utf-8')
    writer = csv.writer(file, delimiter=' ')
    for i in reader:
        writer.writerow(i)
    file.close()


def create_csv():
    """
    Создаёт новый файл и записывает в него столбцы таблицы
    """
    filename = user_interface.get_filename()
    with open(f'{filename}.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'first_name', 'last_name', 'birth_date', 'work_place', 'phone_number']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=' ')
        writer.writeheader()


def check_file_exist(file_name):
    """
    Проверяет наличие файла по указанному пути
    """
    try:
        file = open(f'{file_name}.csv', 'r', newline='', encoding='utf-8')
        file.close()
        return True
    except:
        user_interface.check_file_error()
        return False


def generate_phone_book(file_name):
    """
    Генерирует телефонный справочник и записывает его в файл
    """
    generated_list = generate_list()
    with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8') as file:
        field_names = ['id', 'first_name', 'last_name', 'birth_date', 'work_place', 'phone_number']
        writer = csv.DictWriter(file, fieldnames=field_names, delimiter=' ')
        writer.writeheader()
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(generated_list)
    user_interface.generate_book_success(file_name)


def generate_list():
    """
    Генерирует список строк для генератора телефонного справочника
    """
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
