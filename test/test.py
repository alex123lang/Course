def test_job():
    from src.job import HeadHunterAPI
    hh_api = HeadHunterAPI()
    assert hh_api.url == 'https://api.hh.ru/vacancies'


def test_vacancy():
    from src.vacancy import Vacancy
    vacancy = Vacancy('test', 'https://test.ru', {'from': 30_000}, 'test desc')
    assert vacancy.title == 'test'
    assert vacancy.link == 'https://test.ru'
    assert vacancy.salary == 30_000
    assert vacancy.description == 'test desc'

    assert str(vacancy) == 'Title: test\nLink: https://test.ru\nSalary: 30000\nDescription: test desc'





