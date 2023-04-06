from funcs import create_note

def help():
    print("add -> cоздать заметку")
    print("edit ID -> редактировать заметку")
    print("read -> Читать список")
    print("read ID -> Читать заметку")


def ui():
    com = input("Введите комманду: ")
    if com == "help":
        help()
    elif com == "add":
        create_note()
    else:
        help()
        ui()

ui()