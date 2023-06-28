from abc import ABC, abstractmethod

from vacancy_parser import VacancyParser


class BaseParser(ABC):
    """
    Это базовый класс для анализа вакансий из различных источников.
    """

    @abstractmethod
    def get_vacancies(self, vacancy: str, page_count: int = 10) -> list[dict]:
     """
     Метод извлекает вакансии на основе предоставленных критериев поиска.

     """

     pass

    @abstractmethod
    def convert_vacancies(self, items: list[dict]) -> list[VacancyParser]:
        """
       Преобразует список словарей вакансий в список объектов VacancyParser.
        """

        pass
