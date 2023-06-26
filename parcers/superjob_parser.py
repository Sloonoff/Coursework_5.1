import requests

from .base_parser import BaseParser
from .vacancy_parser import VacancyParser


class SuperJobAPI(BaseParser):
	"""
	doc
	"""

	vac_url = 'https://api.superjob.ru/2.0/vacancies/'

	def __init__(self, api_key: str):
		"""
		doc

		:param api_key:
		"""

		super().__init__()
		self.headers = {'X-Api-App-Id': api_key}
		self.items_name = 'objects'
		self.profession_name = 'profession'
		self.url_name = 'link'

	def get_vacancies(self, vacancy: str, page_count: int = 10) -> list:
		"""
		doc

		:param vacancy:
		:param page_count:
		:return:
		"""

		result = []
		for page_num in range(page_count):
			params = {'keyword': vacancy, 'page': page_num}
			res = requests.get(self.vac_url, params=params, headers=self.headers)

			try:
				if len(res.json()['objects']) == 0:
					raise ValueError(f'Недопустимая страница: {page_num}')

			except ValueError:
				break
			else:
				result.extend(res.json()['objects'])

		return result

	def convert_vacancies(self, items: list[dict]) -> list[VacancyParser]:
		"""
		doc

		:param items:
		:return:
		"""

		result = []
		for item in items:
			if item.get('currency') and item['currency'] != 'rub':
				continue
			else:
				salary_from = item['payment_from']
				salary_to = item['payment_to']
				salary_currency = item['currency']
				requirement = item['candidat']

			name = item['profession']
			url = item['link']

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
