import json

from classes.HH_API import HeadHunter
from classes.SJ_API import SuperJob
from classes_file import JsonAppender
from vacancy_class import VacancyWork


def sorting_vac(vacancies):
    """
    Метод для сортировки вакансий по максимальной оплате.
    Записывает отсортированные данные в json файл
    """
    vacancies_list = []
    sort_vacancies = sorted(vacancies, key=lambda vacancy: vacancy['salary_to'], reverse=True)
    for vacancy in sort_vacancies:
        vacancies_list.append(f"""Название вакансии: {vacancy['name_vacancy']}
Наименование работодателя: {vacancy['employer_name']}
Ссылка на вакансию: {vacancy['url']}
Заработная плата от {vacancy['salary_from']}, до {vacancy['salary_to']}""")
    with open('sort.json', 'w') as f:
        json.dump(sort_vacancies, f, indent=1, ensure_ascii=False)
    return vacancies_list


def top_vacancies(vacancies):
    pass


def user_interaction():
    """
    Функция для взаимодействия с пользователем.
    Позволяет выбрать платформу, с которой получать информацию,
    вводить запрос для поиска вакансии по её названию,
    получить топ вакансий и в отсортированном виде.
    """
    choice = input('''
Выберите платформу на которой будем проводить поиск вакансий:
1 - HeadHunter
2 - SuperJob
0 - Выйти из поиска
''')
    if choice == '1':
        print('Выбран HeadHunter')
        word = input('''Введите название вакансии:\n''').lower()
        print('Загрузка вакансий с HeadHunter...')
        all_hh_vacancies = HeadHunter().get_vacancies(word)
        hh_vac_with_salary = HeadHunter().structuring_vacancies(all_hh_vacancies)
        sorting_list = sorting_vac(hh_vac_with_salary)
        JsonAppender().add_vacancy(word, sorting_list)
        for vacancy in hh_vac_with_salary:
            vacancy_class = VacancyWork(vacancy['name_vacancy'], vacancy['employer_name'], vacancy['url'],
                                        vacancy['salary_from'], vacancy['salary_to'])
            print(f'{vacancy_class}s\n')
    elif choice == '2':
        print('Выбран SuperJob')
        word = input('''Введите название вакансии:\n''').lower()
        print('Загрузка вакансий с SuperJob...')
        all_sj_vacancies = SuperJob().get_vacancies(word)
        sj_vac_with_salary = SuperJob().structuring_vacancies(all_sj_vacancies)
        sorting_list = sorting_vac(sj_vac_with_salary)
        JsonAppender().add_vacancy(word, sorting_list)
        for vacancy in sj_vac_with_salary:
            vacancy_class = VacancyWork(vacancy['name_vacancy'], vacancy['employer_name'], vacancy['url'],
                                        vacancy['salary_from'], vacancy['salary_to'])
            print(f'{vacancy_class}s\n')
    else:
        print('Возвращайтесь снова!')
        quit()
