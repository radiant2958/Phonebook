from typing import List, Dict, Optional
"""Класс для управления телефонным справочником.
    
    Attributes:
        filename (str): Путь к файлу с данными справочника.
        entries (List[Dict[str, str]]): Список записей справочника.
"""
class PhoneBook:

    def __init__(self, filename: str):
        """Инициализация телефонного справочника с загрузкой данных."""
        self.filename = filename
        self.entries: List[Dict[str, str]] = self.load()

    def load(self) -> List[Dict[str, str]]:
        """Загружает записи справочника из файла.
        
        Returns:
            List[Dict[str, str]]: Список записей справочника.
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return [eval(line) for line in file.readlines()]
        except FileNotFoundError:
            return []

    def save(self):
        """Сохраняет текущие записи справочника в файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            for entry in self.entries:
                file.write(f"{entry}\n")

    def add_entry(self, entry: Dict[str, str]):
        """Добавляет новую запись в справочник.

        Args:
            entry (Dict[str, str]): Словарь с данными новой записи.
        """
        self.entries.append(entry)

    def edit_entry(self, index: int, new_entry: Dict[str, str]):
        """Редактирует существующую запись в справочнике.

        Args:
            index (int): Индекс редактируемой записи.
            new_entry (Dict[str, str]): Словарь с обновленными данными записи.
        """
        if 0 <= index < len(self.entries):
            self.entries[index] = new_entry

    def delete_entry(self, index: int):
        """Удаляет запись из справочника.

        Args:
            index (int): Индекс удаляемой записи.
        """
        if 0 <= index < len(self.entries):
            self.entries.pop(index)

    def search_entries(self, search_criteria: Dict[str, str]) -> List[Dict[str, str]]:
        """Ищет записи, соответствующие заданным критериям.

        Args:
            search_criteria (Dict[str, str]): Словарь с критериями поиска.

        Returns:
            List[Dict[str, str]]: Список найденных записей.
        """
        results = self.entries
        for key, value in search_criteria.items():
            if value:
                results = [entry for entry in results if value.lower() in entry.get(key, '').lower()]
        return results