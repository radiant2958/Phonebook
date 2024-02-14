from controller import Controller
from model import PhoneBook

def main():
    """Основная точка входа в программу."""
    phonebook = PhoneBook("phonebook.txt")
    controller = Controller(phonebook)
    controller.run()

if __name__ == "__main__":
    main()
