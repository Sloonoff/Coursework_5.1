from base_parser import BaseParser


class SuperJobAPI(BaseParser):
	def __init__(self):
		super().__init__()
		self.vac_url = 'https://api.superjob.ru/2.0/vacancies/'
		self.vac_param_name = 'keyword'
		self.api_key = 'v3.r.129465934.5e3b33d356e8a78d8bcfb17b1b458c78ece00fdd.a2eb0cc4fe4b77c6fcfbcb10e64fe935e4fb52c1'
		self.headers = {'X-Api-App-Id': self.api_key}
		self.items_name = 'objects'
		self.profession_name = 'profession'
		self.url_name = 'link'
		self.salary_to_name = 'payment_to'
		self.salary_from_name = 'payment_from'
		self.salary_currency_name = 'currency'
		self.requirements_name = 'candidat'
