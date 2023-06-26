from abc import ABC, abstractmethod

from vacancy_parser import VacancyParser


class BaseParser(ABC):
	"""
	doc
	"""

	@abstractmethod
	def get_vacancies(self, vacancy: str, page_count: int = 10) -> list[dict]:
		"""
		doc

		:param vacancy:
		:param page_count:
		:return:
		"""

		pass

	@abstractmethod
	def convert_vacancies(self, items: list[dict]) -> list[VacancyParser]:
		"""
		doc

		:param items:
		:return:
		"""

		pass
