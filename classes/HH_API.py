from classes.abs_class_api import ApiWork
import requests


class HeadHunter(ApiWork):
    """
    Класс для работы с сайтом HeadHunter по API,
    наследуемый от абстрактного класса ApiWork.
    """

    def get_vacancies(self, keyword: str):
        """Метод для получения вакансий."""
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword, 'page': 0, 'per_page': 100}
        response = requests.get(url, params=params)
        vacancies = response.json()
        return vacancies

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
