from settings import *

# def menu():
#     while True:
#         print('''
# Choose a number:
# 1 - Создать файл
# 2 - Просмотр файла
# 3 - Добавить информацию
# X - Quit''')
#
#         choice = input(': ')
#         print('-' * 15)
#
#         if choice == '1':
#             create_file()
#         elif choice == '2':
#             show_data()
#         elif choice == '3':
#             add_info()
#         elif choice == 'X':
#             print('Exit')
#             break
#         else:
#             print('Wrong choice. Try again!')

def menu(option):
    options = {
        '1': create_file()
        '2': show_info()
        '3': add_info()
        'X': quit()
    }
    return options[option]
def run():
    option_choice = user_choice()
    menu(option_choice)

run()
