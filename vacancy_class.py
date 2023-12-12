class VacancyWork:
    """
    Класс для работы с вакансиями.
    Имеет методы сравнения вакансий по зарплате.
    """
    def __init__(self, vacancy_name, employer_name, url, salary_from, salary_to):
        self.vacancy_name = vacancy_name
        self.employer_name = employer_name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
