from settings import *


def menu():
    while True:
        choice = user_interface.user_choice()
        print()
        if choice == '1':
            model.create_csv()
        elif choice == '2':
            model.view_row()
        elif choice == '3':
            model.create_row()
        elif choice == '4':
            model.change_row()
        elif choice == 'x':
            print('Exit')
            break
        else:
            print('Wrong choice. Try again!')
        print()


def run():
    menu()
