from src.abstract import AbstractVacancyStorage
import json


class JSONSaver(AbstractVacancyStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            json.dump(vars(vacancy), file, ensure_ascii=False)
            file.write('\n')

    def get_vacancies(self, criteria):
        pass

    def delete_vacancy(self, vacancy):
        pass

