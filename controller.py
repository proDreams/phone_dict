from settings import *

file = ''


def menu():
    while True:
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
            exit()
        else:
            user_interface.menu_error()
        user_interface.new_line()


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
