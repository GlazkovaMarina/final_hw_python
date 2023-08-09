from datetime import datetime

def createNote():
    note = { 'id': 0, 'name': 'New note', 'body': 'test note', 'date': '1.1.2023', 'time': '00:00'
}
    note['id'] = 0
    note['name'] = input("Введите название: ")
    note['body'] = input("Введите текст заметки: ")
    now = datetime.now()
    note['date'] = "{}.{}.{}".format(now.day, now.month, now.year)
    note['time'] = "{}:{}".format(now.hour, now.minute)
    print(note)
    return note

def main():
    choise = 0
    while choise != 6:
        choise = int(input("Выберите действие, нажав соответствующую цифру:\n1 - создание новой заметки,\n2 - редактирование заметки,\n3 - удаление заметки,\n4 - просмотр всех заметок,\n5 - просмотр заметки по выбранной дате\n6 - завершение работы с заметками: "))
        if choise == 1:
          createNote()