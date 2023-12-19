import os
import json
import shutil


def delete_everything_in_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        os.mkdir(folder_path)
    except FileNotFoundError:
        os.mkdir(folder_path)


def get_vacancy_from_salary(vacancy_list, salary_from, salary_to):
    """
    Метод для получения вакансий по параметрам
    :param salary_from: Зарплата от "значение"
    :param salary_to: Зарплата до "значемние"
    """
    sorted_list = []
    for i in vacancy_list:
        if salary_from <= i['salary_to'] <= salary_to:
            sorted_list.append(i)
    return sorted_list


def sorting_vac(vacancies, vacancy_name):
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
    with open(f'user_requests/sort_{vacancy_name}.json', 'w') as f:
        json.dump(sort_vacancies, f, indent=4, ensure_ascii=False)
    return vacancies_list
