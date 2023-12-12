from classes_api import HeadHunter, SuperJob
from utils import user_interaction
from classes_file import JsonAppender


def main():
    pass


if __name__ == '__main__':
    hh_vacancies = HeadHunter().get_vacancies('developer')
    hh_dicts = HeadHunter().structuring_vacancies(hh_vacancies)
    JsonAppender().add_vacancy('developer', hh_dicts)
    print(hh_dicts)
