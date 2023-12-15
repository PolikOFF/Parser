from classes.HH_API import HeadHunter
from classes.SJ_API import SuperJob
from classes.classes_file import JsonAppender
from classes.vacancy_class import VacancyWork
from utils import sorting_vac, get_vacancy_from_salary


def user_interaction():
    """
    Функция для взаимодействия с пользователем.
    Позволяет выбрать платформу, с которой получать информацию,
    вводить запрос для поиска вакансии по её названию,
    получить топ вакансий и в отсортированном виде.
    """
    # Поиск на определенной платформе.
    choice = input('''
Выберите платформу на которой будем проводить поиск вакансий:
"1" - HeadHunter
"2" - SuperJob
"0" - Выйти из поиска
''')
    if choice == '1':
        print('Выбран HeadHunter')
        word = input('''Введите название вакансии:\n''').lower()
        print('Загрузка вакансий с HeadHunter...')
        all_hh_vacancies = HeadHunter().get_vacancies(word)
        vac_with_salary = HeadHunter().structuring_vacancies(all_hh_vacancies)
        sorting_list = sorting_vac(vac_with_salary, word)
        JsonAppender().add_vacancy(word, vac_with_salary)
        for vacancy in vac_with_salary:
            vacancy_class = VacancyWork(vacancy['name_vacancy'], vacancy['employer_name'], vacancy['url'],
                                        vacancy['salary_from'], vacancy['salary_to'])
            print(f'{vacancy_class}\n')
    elif choice == '2':
        print('Выбран SuperJob')
        word = input('''Введите название вакансии:\n''').lower()
        print('Загрузка вакансий с SuperJob...')
        all_sj_vacancies = SuperJob().get_vacancies(word)
        vac_with_salary = SuperJob().structuring_vacancies(all_sj_vacancies)
        sorting_list = sorting_vac(vac_with_salary, word)
        JsonAppender().add_vacancy(word, sorting_list)
        for vacancy in vac_with_salary:
            vacancy_class = VacancyWork(vacancy['name_vacancy'], vacancy['employer_name'], vacancy['url'],
                                        vacancy['salary_from'], vacancy['salary_to'])
            print(f'{vacancy_class}\n')
    else:
        print('Возвращайтесь снова!')
        quit()
    # Вывод информации, нужной пользователю.
    choice = input('''Для того чтобы увидеть отсортированный список по убыванию зарплат нажмите - "1"
Вывести отсортированный список вакансии по параметрам зарплаты "от" и "до" нажмите - "2"
Для продолжения нажмите - "3"\n''')
    if choice == '1':
        for i in sorting_list:
            print(f'{i}\n')
    elif choice == '2':
        salary_from = int(input('ВВедите от какой суммы\n'))
        salary_to = int(input('Введите до какой суммы\n'))
        sorting_by_user_parameters = get_vacancy_from_salary(vac_with_salary, salary_from, salary_to)
        reduction_to_the_desired_form = sorting_vac(sorting_by_user_parameters, word)
        for vacancy in reduction_to_the_desired_form:
            print(vacancy)
    elif choice == '3':
        print('Продолжаем')

    answer = input('Желаете увидеть топ вакансий?\nY/N\n').lower()
    if answer == 'y':
        count_vacancies = int(input('Введите количество вакансий\n'))
        for vacancy in sorting_list[0:count_vacancies]:
            print(f'{vacancy}\n')
            print("На этом мы прощаемся! Хорошего дня!")
    elif answer == 'n':
        print('На этом мы прощаемся! Хорошего дня!')
        quit()
