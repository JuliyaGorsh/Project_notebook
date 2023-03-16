

import notebook as nb
from datetime import datetime as dt

def main_menu():
    print('Выберите команду меню:')
    print('1. Показать блокнот')
    print('2. Загрузить заметки')
    print('3. Сохранить заметку')
    print('4. Добавить заметку')
    print('5. Изменить заметку')
    print('6. Удалить заметку')
    print('7. Найти заметку')
    print('0. Выйти из приложения\n')
    return input_menu()

def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(1, 8) or choice == 0:
                return choice
            else:
                print('Такого пункта меню нет. Внимательнее, пожалуйста')
        except:
            print('Ошибка ввода. Введите корректный пункт меню')
