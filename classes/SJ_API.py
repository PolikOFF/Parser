import os

from classes.abs_class_api import ApiWork
import requests

API_SJ = os.getenv('SuperJob_API_KEY')


class SuperJob(ApiWork):
    """
    Класс для работы с сайтом SuperJob по API,
    наследуемый от абстрактного класса ApiWork.
    """

    def __init__(self):
        self.API_KEY = {'X-Api-App-Id': API_SJ}

    def get_vacancies(self, keyword: str):
        """Метод для получения вакансий."""
        url = 'https://api.superjob.ru/2.0/vacancies/'
        params = {'keyword': keyword, 'page': 0, 'per_page': 100}
        response = requests.get(url, headers=self.API_KEY, params=params)
        return response.json()

    def structuring_vacancies(self, all_vacancies):
        """
        Метод для структурирования данных вакансии,
        для последующего использования.
        Используются вакансии в которых указана заработная плата.
        """
        vacancies_with_salary = []
        vacancies_dicts = []
        # Достаем нужные сведения из вакансии
        for i in range(len(all_vacancies)):
            if all_vacancies['objects'][i]['payment_from'] != 0 and all_vacancies['objects'][i]['payment_to'] != 0:
                vacancies_with_salary.append([all_vacancies['objects'][i]['profession'],
                                              all_vacancies['objects'][i]['client']['title'],
                                              all_vacancies['objects'][i]['link'],
                                              all_vacancies['objects'][i]['payment_from'],
                                              all_vacancies['objects'][i]['payment_to']]
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