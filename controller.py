import add_to_db
import extract
import view

def phone_book():
    menu = view.main_menu()
    while menu != 3:
        match menu:
            case 1:
                phone_data = view.write_data()
                add_to_db.add_to_txt(phone_data)
                add_to_db.add_to_csv(phone_data)
            case 2:
                extract.full_output()
            case 3:
                lastname = view.search_data()
                extract.find_data(lastname)