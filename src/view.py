from funcs import *

def help():
    print("add -> cоздать")
    print("edit -> редактировать")
    print("read -> читать")
    print("rm -> удалить")
    print("exit -> выход")


def ui():
    while (True):
        com = input("Введите комманду: ")
        if com == "help":
            help()
        elif com == "add":
            create_note()
        elif com == "read":
            list_note()
            read = input("Введите ID: ")
            read_id_note(read)
        elif com == "edit":
            list_note()
            edit = input("Введите ID: ")
            try: # Обернул в try except потому что с пустым вводом выдает ошибку
                edit_id_note(edit)
            except:
                print("Ошибка при вводе!!!")
        elif com == "rm":
            list_note()
            edit = input("Введите ID: ")
            try:
                remove_id_note(edit)
            except:
                print("Ошибка при вводе!!!")


        elif com == "exit":
            break
        else:
            help()