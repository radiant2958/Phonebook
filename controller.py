from model import PhoneBook
from view import show_menu, get_contact_details, select_contact_index, show_entries, show_search_criteria
import sys

"""Класс контроллера для управления взаимодействием между моделью и представлением."""

class Controller:
    def __init__(self, phonebook: PhoneBook):
        """Инициализирует контроллер с указанным телефонным справочником.

            Args:
                phonebook (PhoneBook): Экземпляр телефонного справочника.
        """
        self.phonebook = phonebook

    def run(self):
        """Запускает основной цикл программы для взаимодействия с пользователем."""
       
        while True:
             choice = show_menu()
             match choice:
                case 1:
                    show_entries(self.phonebook.entries)
                case 2:
                    new_entry = get_contact_details()
                    self.phonebook.add_entry(new_entry)
                    self.phonebook.save()
                case 3:
                    index = select_contact_index(self.phonebook.entries)
                    new_entry = get_contact_details()
                    self.phonebook.edit_entry(index, new_entry)
                    self.phonebook.save()
                case 4:
                    index = select_contact_index(self.phonebook.entries)
                    self.phonebook.delete_entry(index)
                    self.phonebook.save()
                case 5:
                    criteria = show_search_criteria()
                    results = self.phonebook.search_entries(criteria)
                    show_entries(results)
                case 6:
                    sys.exit()
                case _:
                    print("Неверный выбор, попробуйте еще раз")
