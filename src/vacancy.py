class Vacancy:
    name: str
    link: str
    salary: dict
    description: str

    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary.get('from') if salary and salary.get('from') else 0
        self.description = description if description else "Описание отсутствует"

    def __str__(self):
        return f"Title: {self.title}\nLink: {self.link}\nSalary: {self.salary}\nDescription: {self.description}"

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary




