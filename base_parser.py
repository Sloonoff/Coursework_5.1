import requests

from vacancy_parser import VacancyParser


class BaseParser:
	vac_param_name = None
	items_name = None
	profession_name = None
	url_name = None
	salary_from_name = None
	salary_to_name = None
	salary_currency_name = None
	requirements_name = None

	vac_url = None
	app_key = None

	headers = None
	params = None

	def __init__(self):
		pass

	def get_vacancies(self, vacancy: str, page_count: int = 10):
		result = []
		for page_num in range(page_count):
			params = {self.vac_param_name: vacancy, 'page': page_num, 'api_key': self.app_key}
			res = requests.get(self.vac_url, params=params, headers=self.headers)

			if res.json().get('bad_argument') or len(res.json()[self.items_name]) == 0:
				raise ValueError(f'Недопустимая страница: {page_num}')

			result.extend(res.json()[self.items_name])
		return result

	def convert_vacancies(self, items: list):
		result = []
		for item in items:
			if item.get(self.salary_currency_name):
				if item[self.salary_currency_name] != 'rub':
					continue
				else:
					salary_from = item[self.salary_from_name]
					salary_to = item[self.salary_to_name]
					salary_currency = item[self.salary_currency_name]
					requirement = item[self.requirements_name]
			else:
				if item.get('salary'):
					if item['salary'][self.salary_currency_name] != 'RUR':
						continue
					else:
						if isinstance(item['salary'][self.salary_from_name], int):
							print(type(item['salary'][self.salary_from_name]))
							salary_from = item['salary'][self.salary_from_name]
						else:
							salary_from = 0
						if isinstance(item['salary'][self.salary_to_name], int):
							print(type(item['salary'][self.salary_to_name]))
							salary_to = item['salary'][self.salary_to_name]
						else:
							salary_to = 0
						if isinstance(item['salary'][self.salary_currency_name], str):
							salary_currency = item['salary'][self.salary_currency_name]
						else:
							salary_currency = None
						if isinstance(item['snippet'][self.requirements_name], str):
							requirement = item['snippet'][self.requirements_name]
						else:
							requirement = None
				else:
					salary_from, salary_to, salary_currency, requirement = 0, 0, 0, 0

			# Собираем параметры
			name = item[self.profession_name]
			url = item[self.url_name]

			# Передаём в класс Вакансии
			vac = VacancyParser(
				name,
				url,
				salary_from,
				salary_to,
				salary_currency,
				requirement
			)
			result.append(vac)  # Собираем в результирующий список

		return result
