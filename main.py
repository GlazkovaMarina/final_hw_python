from datetime import datetime


def createNode():
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

createNode()