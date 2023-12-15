from abc import ABC, abstractmethod


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
