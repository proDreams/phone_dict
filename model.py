import csv
import user_interface

def view_row():
    with open('db.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            user_interface.print_output(i)
        exit()

def create_row():
    with open('db.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            user_interface.print_output(i)


def change_row():
    with open('db.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            user_interface.print_output(i)

def create_csv():
    return 0
