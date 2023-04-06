import datetime
from data_buse import save_note, read_note, edit_note

try:
    id = int(read_note()[-2][0]) + 1 # id для заметок начинает с последней заметки
except:
    id = 1 # Если нет заметок то начинаеться с 1


def create_note(): # Создание заметки, тут мы делаем список, заполняем его и записываем результат в фаил
    global id
    note = []
    note.append(str(id))
    id += 1
    note.append(input("Введите название заметки: "))
    note.append(input("Введите тело заметки: "))
    note.append(str(datetime.datetime.now().today().replace(microsecond=0)))
    result = [note] # Список в списке для нормального сохранения
    save_note(result) # Метод для записи
    print("Заметка успешно сохранена")

def list_note(): # Распичатывает список
    arr = read_note()
    for i in arr[:-1]:
        print(f"{i[0]}. {i[1]}")

def read_id_note(id): # Печать заметки (обращение по id)
    arr = read_note()
    for i in arr:
        if i[0] == id:
            print("----------")
            for j in i[1:]:
                print('\n' + j + '\n')
            print("----------")


def edit_id_note(id):# Редактирование заметки (обращение по id)
    arr = read_note()
    for i in arr:
        if i[0] == id:
            i[1] = input("Введите название: ")
            i[2] = input("Введите тело заметки: ")
    arr.pop()
    edit_note(arr)

def remove_id_note(id):# Редактирование заметки (обращение по id)
    arr = read_note()
    for i in arr:
        if i[0] == id:
            arr.remove(i)
            print(arr)
            arr.pop()
            edit_note(arr)