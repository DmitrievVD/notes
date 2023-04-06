import datetime
ID = 1

def create_note(ID = ID):
    note = []
    note.append(ID)
    ID += 1
    note.append(input("Введите название заметки: "))
    note.append(input("Введите тело заметки: "))
    note.append(datetime.datetime.now().today().replace(microsecond=0))
    for i in note:
        print(i)
