import datetime
from data_buse import save_note


id = 1

def create_note(id = id):
    note = []
    note.append(str(id))
    id += 1
    note.append(input("Введите название заметки: "))
    note.append(input("Введите тело заметки: "))
    note.append(str(datetime.datetime.now().today().replace(microsecond=0)))
    result = [note]
    save_note(result)

create_note()