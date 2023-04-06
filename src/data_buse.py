
import csv

def edit_note(note):
    with open('notes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(note)


def save_note(note):
    with open('notes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(note)

def read_note():
    try:
        with open("notes.csv", "r") as file:
            str_file = file.read().split("\n")
            result = []
            for i in str_file:
                result.append(i.split(","))
            return result
    except:
        print("Заметки еще нету!!!")
