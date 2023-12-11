class VacancyWork:
    """
    Класс для работы с вакансиями.
    Имеет методы сравнения вакансий по зарплате.
    """
    def __init__(self, name, url, external_id, salary_from, salary_to):
        self.name = name
        self.url = url
        self.external_id = external_id
        self.salary_from = salary_from
        self.salary_to = salary_to
