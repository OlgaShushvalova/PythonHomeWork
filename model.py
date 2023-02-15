path = 'notes.csv'
contacts = []


def read_file():
    global contacts
    with open(path) as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    return contacts


def get_contacts():
    global contacts
    return contacts


def add_contact():
    global contacts
    id = input('Введите номер: ')
    title = input('Введите заголовок: ')
    body = input('Введите содержание: ')
    date_time = input('Введите дату и время:')
    contacts.append(';'.join([id, title, body, date_time]))


def save_file():
    global contacts
    with open(path, 'w', encoding='utf_8') as f:
        pass
