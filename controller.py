import view
import model


def start():
    while True:
        command = view.show_menu()
        match command:
            case '1':
                model.add_contact()
            case '2':
                view.show_contacts(model.get_contacts())
            case '0':
                break
