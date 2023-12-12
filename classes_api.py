from abc import ABC, abstractmethod
import requests

API_SJ = 'v3.r.112557166.6ccf64c3128111d522ffd74ec395f85805cdcfe9.a22bdca6107a065edd5f4a4704813f7058ef98eb'


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


class HeadHunter(ApiWork):
    """
    Класс для работы с сайтом HeadHunter по API,
    наследуемый от абстрактного класса ApiWork.
    """
    vacancies = []

    def get_vacancies(self, keyword: str):
        """Функция для получения вакансий."""
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword, 'page': 0, 'per_page': 100}
        response = requests.get(url, params=params)
        all_vacancies = response.json()
        return all_vacancies

    def structuring_vacancies(self, all_vacancies):
        """
        Метод для структурирования данных вакансии,
        для последующего использования.
        Используются вакансии в которых указана заработная плата.
        """
        vacancies_with_salary = []
        vacancies_dicts = []
        vacancies_dict = {}
        # Достаем нужные сведения из вакансии
        for i in range(len(all_vacancies)):
            if all_vacancies['items'][i]['salary'] is not None:
                vacancies_with_salary.append([all_vacancies['items'][i]['name'],
                                             all_vacancies['items'][i]['employer']['name'],
                                             all_vacancies['items'][i]['apply_alternate_url'],
                                             all_vacancies['items'][i]['salary']['from'],
                                             all_vacancies['items'][i]['salary']['to']]
                                             )
        # Составляем словарь из данных, форматируя зарплату "от" и "до"
        for i in vacancies_with_salary:
            vacancies_dict = {
                'name_vacancy': i[0],
                'employer_name': i[1],
                'url': i[2],
                'salary_from': i[3],
                'salary_to': i[4]
            }
            if vacancies_dict['salary_from'] is None:
                vacancies_dict['salary_from'] = 0
            elif vacancies_dict['salary_to'] is None:
                vacancies_dict['salary_to'] = vacancies_dict['salary_from']
            vacancies_dicts.append(vacancies_dict)
        return vacancies_dicts


class SuperJob(ApiWork):
    """
    Класс для работы с сайтом SuperJob по API,
    наследуемый от абстрактного класса ApiWork.
    """
    vacancies = []

    def __init__(self):
        self.API_KEY = {'X-Api-App-Id': API_SJ}

    def get_vacancies(self, keyword: str):
        """Функция для получения вакансий."""
        url = 'https://api.superjob.ru/2.0/vacancies/params'
        params = {'text': keyword, 'count': 1, 'page': 0, 'per_page': 10}
        response = requests.get(url, headers=self.API_KEY, params=params)
        return response.json()

    def structuring_vacancies(self, vacancies):
        """
                Метод для структурирования данных вакансии,
                для последующего использования.
                Используются вакансии в которых указана заработная плата.
                """
        pass
