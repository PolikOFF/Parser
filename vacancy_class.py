class VacancyWork:
    """
    Класс для получения информации по вакансиям.
    """
    def __init__(self, vacancy_name, employer_name, url, salary_from, salary_to):
        self.vacancy_name = vacancy_name
        self.employer_name = employer_name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        return f'''Название вакансии: {self.vacancy_name}\nНаименование работодателя: {self.employer_name}
Ссылка на вакансию: {self.url}\nЗаработная плата от {self.salary_from} до {self.salary_to}'''
