from abc import ABC, abstractmethod
import json


class JobVacancyAppender(ABC):
    """Абстрактный класс для работы со списками вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy_name, vacancy):
        pass

    @abstractmethod
    def load_vacancy(self, value):
        pass

    @abstractmethod
    def delete_vacancy(self, value):
        pass


class JsonAppender(JobVacancyAppender):
    """Класс для использования данных с json'ом"""
    def add_vacancy(self, vacancy_name, vacancy):
        """
        Метод сохранения информации в json файл.
        При отсутствии - файл создается заново,
        при наличии - перезаписывается.
        """
        with open(f'user_requests/{vacancy_name}.json', 'w') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=1)

    def load_vacancy(self, value):
        value = value.lower()
        with open(f'{value}', 'r') as file:
            pass

    def delete_vacancy(self, value):
        pass


class CSVAppender(JobVacancyAppender):

    def add_vacancy(self, vacancy_name, vacancy):
        pass

    def load_vacancy(self, value):
        pass

    def delete_vacancy(self, value):
        pass
