from abc import ABC, abstractmethod
import json
import os


class JobVacancyWork(ABC):
    """Абстрактный класс для работы со списками вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy_name, vacancy):
        pass

    @abstractmethod
    def load_vacancy(self, value):
        pass


class JsonAppender(JobVacancyWork):
    """Класс для использования данных с json'ом"""
    def add_vacancy(self, vacancy_name, vacancy):
        """
        Метод сохранения информации в json файл.
        При отсутствии - файл создается заново,
        при наличии - перезаписывается.
        """
        with os.path.join(f'user_requests/{vacancy_name}.json', 'w') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def load_vacancy(self, value):
        """
        Метод для открытия файла json
        """
        value = value.lower()
        with os.path.join(f'{value}.json', 'r') as file:
            a = json.load(file, indent=4)
            print(a)


class CSVAppender(JobVacancyWork):

    def add_vacancy(self, vacancy_name, vacancy):
        pass

    def load_vacancy(self, value):
        pass
