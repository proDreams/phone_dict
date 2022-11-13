import model
import user_interface
from settings import *

file = ''


def menu():
    while True:
        choice = user_interface.mode_choice()
        print()
        if choice == '1':
            model.create_csv()
        elif choice == '2':
            model.view_row(file)
        elif choice == '3':
            model.create_row(file)
        elif choice == '4':
            model.change_row(file)
        elif choice == '5':
            model.delete_row(file)
        elif choice == 'x':
            print('Exit')
            break
        else:
            print('Wrong choice. Try again!')
        print()


def choice_file():
    global file
    file = user_interface.choice_file_prints()
    if file == 'new_file':
        model.create_csv()
    elif file == '':
        file = 'db'
        menu()
    elif model.check_file_exist(file):
        menu()
    else:
        choice_file()


def run():
    choice_file()
