import datetime
from data_buse import save_note, read_note, edit_note

try:
    id = len(read_note()) + 1
except:
    id = 1


def create_note():
    global id
    note = []
    note.append(str(id))
    id += 1
    note.append(input("Введите название заметки: "))
    note.append(input("Введите тело заметки: "))
    note.append(str(datetime.datetime.now().today().replace(microsecond=0)))
    result = [note]
    save_note(result)
    print("Заметка успешно сохранена")

def list_note():
    arr = read_note()
    for i in arr[:-1]:
        print(f"{i[0]}. {i[1]}")

def read_id_note(id):
    arr = read_note()
    for i in arr:
        if i[0] == id:
            print("----------")
            for j in i[1:]:
                print('\n' + j + '\n')
            print("----------")


def edit_id_note(id):
    arr = read_note()
    for i in arr:
        if i[0] == id:
            i[1] = input("Введите название: ")
            i[2] = input("Введите тело заметки: ")
    arr.pop()
    edit_note(arr)