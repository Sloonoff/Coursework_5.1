import requests

from .base_parser import BaseParser
from .vacancy_parser import VacancyParser


class HeadHunterAPI(BaseParser):
	"""
	doc
	"""

	vac_url = 'https://api.hh.ru/vacancies'

	def __init__(self):
		"""
		doc
		"""

		super().__init__()

	def get_vacancies(self, vacancy: str, page_count: int = 10) -> list[dict]:
		"""
		doc

		:param vacancy:
		:param page_count:
		:return:
		"""

		result = []
		for page_num in range(page_count):
			params = {'text': vacancy, 'page': page_num}
			res = requests.get(self.vac_url, params=params)
			try:
				if res.json().get('bad_argument'):
					raise ValueError(f'Недопустимая страница: {page_num}')

			except ValueError:
				break
			else:
				result.extend(res.json()['items'])

		return result

	def convert_vacancies(self, items: list[dict]) -> list[VacancyParser]:
		"""
		doc

		:param items:
		:return:
		"""

		result = []
		for item in items:
			if item.get('salary'):
				if item['salary']['currency'] != 'RUR':
					continue
				salary_from = item['salary']['from'] if isinstance(item['salary']['from'], int) else 0
				salary_to = item['salary']['to'] if isinstance(item['salary']['to'], int) else 0
				salary_currency = item['salary']['currency']
				requirement = item['snippet']['requirement']
			else:
				salary_from, salary_to = 0, 0
				salary_currency, requirement = '', ''

			name = item['name']
			url = item['alternate_url']

			vac = VacancyParser(
				name,
				url,
				salary_from,
				salary_to,
				salary_currency,
				requirement
			)
			result.append(vac)

		return result
