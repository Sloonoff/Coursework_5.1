class VacancyParser:
    """
          Создает объект Job с заданными атрибутами.

        Параметры:
        - name (str): Название вакансии.
        - url (str): URL вакансии.
        - salary_from (float): Минимальная зарплата.
        - salary_to (float): Максимальная зарплата.
        - salary_currency (str): Валюта зарплаты.
        - requirement (str): Требования к кандидатам.

        Возвращает:
        - job (Job): Объект Job.
    """

    def __init__(self, name, url, salary_from, salary_to, salary_currency, requirement):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.requirement = requirement

    """
           Сравнивает текущую вакансию с другой вакансией по максимальной зарплате.

           Параметры:
           - other (Job): Вторая вакансия для сравнения.

           Возвращает:
           - result (bool): Результат сравнения:
               - True, если максимальная зарплата текущей вакансии больше максимальной зарплаты другой вакансии.
               - False, в противном случае.
    """

    def __gt__(self, other):
        if self.salary_to == 0 and other.salary_to == 0:
            return self.salary_from > other.salary_from

        return self.salary_to > other.salary_to



    """
        Сравнивает текущую вакансию с другой вакансией по максимальной зарплате.
    """
    def __lt__(self, other):
        if self.salary_to == 0 and other.salary_to == 0:
            return self.salary_from < other.salary_from

        return self.salary_to < other.salary_to

    """
     Сравнивает текущую вакансию с другой вакансией по максимальной зарплате.
    """
    def __eq__(self, other):
        if self.salary_to == 0 and other.salary_to == 0:
            return self.salary_from == other.salary_from

        return self.salary_to == other.salary_to
