from settings import *
import sys

file = ''


def menu():
    flag = True
    while flag:
        choice = user_interface.mode_choice()
        user_interface.new_line()
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
        elif choice == '6':
            model.generate_phone_book(file)
        elif choice == '0':
            choice_file()
        elif choice == 'x':
            user_interface.exit_program()
            flag = False
        else:
            user_interface.menu_error()
        user_interface.new_line()


def choice_file():
    global file
    while True:
        file = user_interface.choice_file_prints()
        if file == '':
            file = 'db'
            break
        elif model.check_file_exist(file):
            break
    menu()


def run():
    choice_file()
