from datetime import datetime

def saveNote(note):
    file = open('notes.txt', 'a')


def createNote():
    note = { 'id': 0, 'name': 'New note', 'body': 'test note', 'date': '1.1.2023', 'time': '00:00'
}
    note['id'] = 0
    note['name'] = input("Введите название: ")
    note['body'] = input("Введите текст заметки: ")
    now = datetime.now()
    note['date'] = now.strftime('%d.%m.%Y')
    note['time'] = now.strftime('%H:%M:%S')
    print('Заметка', note.get('body'), 'под №', note.get('id'), 'c названием', note.get('name'), 'создана в', note.get('time'),  note.get('date'))
    choise = 3
    while (choise != 2):
        try:
            choise = int(input('Если хотите сохранить данную заметку, то нажмите 1, иначе 2: '))
        except ValueError:
            print('Ошибка ввода. Необходимо ввести число 1 или 2!')
        if choise == 1:
            saveNote(note)
            choise = 2

def main():
    choise = 0
    while choise != 6:
        choise = int(input("Выберите действие, нажав соответствующую цифру:\n1 - создание новой заметки,\n2 - редактирование заметки,\n3 - удаление заметки,\n4 - просмотр всех заметок,\n5 - просмотр заметки по выбранной дате\n6 - завершение работы с заметками: "))
        if choise == 1:
          createNote()


main()