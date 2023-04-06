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
            edit_id_note(edit)
        elif com == "rm":
            list_note()
            edit = input("Введите ID: ")
            remove_id_note(edit)



        elif com == "exit":
            break
        else:
            help()