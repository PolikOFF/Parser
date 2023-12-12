from utils import user_interaction


def main():
    user_interaction()
    answer = input('Желаете увидеть отсортированный список?\nY/N(да/нет)').lower()
    if answer == 'y' or 'yes' or 'да' or 'д':
        pass
    elif answer == 'n' or 'no' or 'нет' or 'н':
        pass
    else:
        print('Такого варианта нет')
    answer = input('Желаете увидеть топ вакансий?\nY/N(да/нет)').lower()
    if answer == 'y' or 'yes' or 'да' or 'д':
        pass
    elif answer == 'n' or 'no' or 'нет' or 'н':
        pass
    else:
        print('Такого варианта нет')


if __name__ == '__main__':
    user_interaction()
