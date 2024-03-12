from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class AbstractVacancyStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

