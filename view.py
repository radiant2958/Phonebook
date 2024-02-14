from typing import List, Dict

def show_menu() -> int:
    """Отображает главное меню и запрашивает выбор пользователя.

        Returns:
            int: Выбор пользователя.
    """
    print("\nМеню:")
    menu_list = [
        "Показать все контакты",
        "Добавить новый контакт",
        "Редактировать контакт",
        "Удалить контакт",
        "Поиск контакта",
        "Выйти"
    ]
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item}")
    return int(input("Выберите действие: "))

def get_contact_details() -> Dict[str, str]:
    """Запрашивает у пользователя данные для создания или редактирования контакта.

        Returns:
            Dict[str, str]: Словарь с данными контакта.
    """
    print("\nВведите данные контакта:")
    return {
        "lastname": input("Фамилия: "),
        "firstname": input("Имя: "),
        "organization": input("Организация: "),
        "work_phone": input("Рабочий телефон: "),
        "personal_phone": input("Личный телефон: ")
    }

def select_contact_index(entries: List[Dict[str, str]]) -> int:
    """Позволяет пользователю выбрать контакт для редактирования или удаления.

        Args:
            entries (List[Dict[str, str]]): Список контактов для выбора.

        Returns:
            int: Индекс выбранного контакта.
    """
    for index, entry in enumerate(entries, start=1):
        print(f"{index}. {entry['lastname']} {entry['firstname']}")
    return int(input("Выберите номер контакта: ")) - 1

def show_entries(entries: List[Dict[str, str]]):
    """Отображает список контактов.

        Args:
            entries (List[Dict[str, str]]): Список контактов для отображения.
    """
    if not entries:
        print("Список контактов пуст.")
        return
    for entry in entries:
        print(f"{entry['lastname']} {entry['firstname']}, Организация: {entry['organization']}, Рабочий: {entry['work_phone']}, Личный: {entry['personal_phone']}")

def show_search_criteria() -> Dict[str, str]:
    """Запрашивает критерии поиска у пользователя.

        Returns:
            Dict[str, str]: Словарь с критериями поиска.
    """
    print("\nВведите критерии поиска:")
    return {
        "lastname": input("Фамилия (оставьте пустым, если не используется): "),
        "firstname": input("Имя (оставьте пустым, если не используется): "),
        "organization": input("Организация (оставьте пустым, если не используется): ")
    }
