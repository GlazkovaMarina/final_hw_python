from datetime import datetime
import json
import os

def readNotes():
    if os.path.exists("notes.json"):
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
                for i in data['note']:
                    print(i)
        except OSError:
            print("\nПроизошла ошибка при работе с файлом:(")
    else:
        print("\nЗаметок пока еще не создавалось!\n")
def saveNote(note):
    if os.path.exists("notes.json"):
        try:
            data = {}
            with open('notes.json', 'r') as file:
                data = json.load(file)
                data['note'].append(note)
            with open('notes.json', 'w') as file:
                json.dump(data, file, indent='\t', ensure_ascii=False)
        except OSError:
            print("\nПроизошла ошибка при работе с файлом:(\n")
    else:
        try:
            with open('notes.json', 'w') as file:
                data = {}
                data['note'] = []
                data['note'].append(note)
                json.dump(data, file, indent='\t', ensure_ascii=False)
        except OSError:
            print("\nПроизошла ошибка при работе с файлом:(\n")


def createNote():
    note = { 'id': 0, 'name': 'New note', 'body': 'test note', 'date': '1.1.2023', 'time': '00:00'
}
    id = 0
    if os.path.exists("notes.json"):
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
                id = len(data['note'])
        except OSError:
            print("\nПроизошла ошибка при работе с файлом при считывании id заметок!\n")
    note['id'] = id
    note['name'] = input("Введите название: ")
    note['body'] = input("Введите текст заметки: ")
    now = datetime.now()
    note['date'] = now.strftime('%d.%m.%Y')
    note['time'] = now.strftime('%H:%M:%S')
    print('Заметка', note.get('body'), 'под №', note.get('id'), 'c названием', note.get('name'), 'создана в', note.get('time'),  note.get('date'))
    choise = 3
    while (choise != 2):
        try:
            choise = int(input('\nЕсли хотите сохранить данную заметку, то нажмите 1, иначе 2: '))
        except ValueError:
            print('\nОшибка ввода. Необходимо ввести число 1 или 2!\n')
        if choise == 1:
            saveNote(note)
            choise = 2

def main():
    choise = 0
    while choise != 6:
        try:
            choise = int(input("\nВыберите действие, нажав соответствующую цифру:\n1 - создание новой заметки,\n2 - редактирование заметки,\n3 - удаление заметки,\n4 - просмотр всех заметок,\n5 - просмотр заметки по выбранной дате\n6 - завершение работы с заметками: "))
            if choise < 1 or choise > 6:
                print('\nОшибка ввода. Необходимо ввести число от 1 до 6!\n')
        except ValueError:
            print('\nОшибка ввода. Необходимо ввести число от 1 до 6!\n')
        if choise == 1:
            createNote()
        elif choise == 4:
            readNotes()


main()