from abc import ABC, abstractmethod
import requests


class ApiWork(ABC):
    """
    Абстрактный класс для работы с сайтами
    по вакансиям, с помощью API.
    """
    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass


class HeadHunter(ApiWork):
    """
    Класс для работы с сайтом HeadHunter по API,
    наследуемый от абстрактного класса ApiWork.
    """
    vacancies = []

    def get_vacancies(self, keyword: str):
        """Функция для получения вакансий."""
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword, 'count': 50, 'page': 0, 'per_page': 10}
        response = requests.get(url, params=params)
        return response.json()


class SuperJob(ApiWork):
    """
    Класс для работы с сайтом SuperJob по API,
    наследуемый от абстрактного класса ApiWork.
    """
    vacancies = []

    def __init__(self):
        self.API_KEY = {
                'X-Api-App-Id':
                    'v3.r.112557166.6ccf64c3128111d522ffd74ec395f85805cdcfe9.a22bdca6107a065edd5f4a4704813f7058ef98eb'}

    def get_vacancies(self, keyword: str):
        """Функция для получения вакансий."""
        url = 'https://api.superjob.ru/2.0/vacancies/params'
        params = {'text': keyword, 'count': 1, 'page': 0, 'per_page': 10}
        response = requests.get(url, headers=self.API_KEY, params=params)
        return response.json()
