from classes_api import HeadHunter, SuperJob


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
        word = input('''Введите название вакансии:\n''')
        print('Загрузка вакансий с HeadHunter.')
        hh = HeadHunter().get_vacancies(word)
    elif choice == '2':
        print('Выбран SuperJob')
        word = input('''Введите название вакансии:\n''')
        print('Загрузка вакансий с SuperJob.')
        sj = SuperJob().get_vacancies(word)
    else:
        print('Возвращайтесь снова!')
        quit()
