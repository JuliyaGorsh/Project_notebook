
import data_base
import view
import notebook as nb

def choice_menu(choice):
    match choice:
        case 1:
            view.print_notebook()
        case 2:
            data_base.load_note()
        case 3:
            data_base.save_note()
        case 4:
            nb.add_note()
        case 5:
            nb.change_note()
        case 6:
            nb.remove_note()
        case 7:
            nb.find_note()
        case 0:
            a = input('Вы уверены, что хотите выйти? Перед выходом не забудьте сохранить изменения. (y/n)')
            if a == 'y':
                print('Вы вышли!')
                return True

while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break
