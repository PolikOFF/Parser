from abc import ABC, abstractmethod
import json


class JobVacancyAppender(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def load_vacancy(self, value):
        pass

    @abstractmethod
    def delete_vacancy(self, value):
        pass


class JsonAppender(JobVacancyAppender):

    def add_vacancy(self, vacancy):
        vacancy = vacancy.lower()
        with open(f'{vacancy}', 'w') as file:
            file.write(json.dumps(vacancy))

    def load_vacancy(self, value):
        value = value.lower()
        with open(f'{value}', 'r') as file:
            pass

    def delete_vacancy(self, value):
        pass
