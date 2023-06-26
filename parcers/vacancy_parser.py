class VacancyParser:
	def __init__(self, name, url, salary_from, salary_to, salary_currency, requirement):
		self.name = name
		self.url = url
		self.salary_from = salary_from
		self.salary_to = salary_to
		self.salary_currency = salary_currency
		self.requirement = requirement

	def __gt__(self, other):
		if self.salary_to == 0 and other.salary_to == 0:
			return self.salary_from > other.salary_from

		return self.salary_to > other.salary_to

	def __lt__(self, other):
		if self.salary_to == 0 and other.salary_to == 0:
			return self.salary_from < other.salary_from

		return self.salary_to < other.salary_to

	def __eq__(self, other):
		if self.salary_to == 0 and other.salary_to == 0:
			return self.salary_from == other.salary_from

		return self.salary_to == other.salary_to
