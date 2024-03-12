from src.abstract import AbstractVacancyAPI
import requests


class HeadHunterAPI(AbstractVacancyAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_query):
        params = {
            'text': search_query,
            'per_page': 100
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            raise Exception(f"Failed to fetch vacancies. Status code: {response.status_code}")
