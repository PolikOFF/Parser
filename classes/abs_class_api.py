from abc import ABC, abstractmethod
from classes_file import JsonAppender


class ApiWork(ABC):
    """
    Абстрактный класс для работы с сайтами
    по вакансиям, с помощью API.
    """
    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    @abstractmethod
    def structuring_vacancies(self, all_vacancies):
        pass
