from base_parser import BaseParser


class HeadHunterAPI(BaseParser):
	def __init__(self):
		super().__init__()
		self.vac_url = 'https://api.hh.ru/vacancies'
		self.vac_param_name = 'text'
		self.items_name = 'items'
		self.profession_name = 'name'
		self.url_name = 'alternate_url'
		self.salary_to_name = 'to'
		self.salary_from_name = 'from'
		self.salary_currency_name = 'currency'
		self.requirements_name = 'requirement'
