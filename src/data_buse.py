
import csv
data = [['John', 'Doe', 25], ['Jane', 'Doe', 30], ['Bob', 'Smith', 35]]
def save_note(note):
    with open('notes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(note)

def read_note():
    with open("notes.csv", "r") as file:
        str_file = file.write()
        print(str_file)

save_note(data)