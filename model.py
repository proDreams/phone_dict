import csv


def view_row():
    with open('db.csv', 'r') as file:
        file.readline()


def create_row():
    with open('db.csv', 'a') as file:
    file.readline()


def change_row():
    with open('db.csv', 'a') as file:
    file.readline()


def create_csv():
    return 0
