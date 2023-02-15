def show_menu():
    question = 'Введите необходимую команду: \
    \n1: Создать заметку \
    \n2: Показать заметки \
    \n3: Редактировать заметку \
    \n4: Удалить заметку \
    \n5: Выход \
    \n'
    command = input(question)
    return command


def show_contacts(contacts: list):
    [print(contact) for contact in contacts]
