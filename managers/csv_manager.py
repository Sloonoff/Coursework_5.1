import os
import csv

from work_sercher.parcers.vacancy_parser import VacancyParser


class CSVFileManager:
	"""
	Данные функции работают с файлами CSV.
	"""

	path = './result.csv'
	headers = ['name', 'url', 'salary_from', 'salary_to', 'requirements']

	def __init__(self, path: str = None):
		"""
		Инициализации объекта и определения пути к файлу CSV.

		"""

		if path:
			self.path = path

	def load_to(self, vacancies: list[VacancyParser]) -> None:
		"""
		Запись данных в файл CSV. Получает список вакансий и записывает их в CSV-файл.

		"""

		with open(self.path, 'w', encoding='utf-8') as fp:
			writer = csv.writer(fp, dialect='excel', delimiter=';')
			writer.writerow(self.headers)

			for vac in vacancies:
				row = [vac.name, vac.url, vac.salary_from, vac.salary_to, vac.requirement]
				writer.writerow(row)

	def load_from(self, user_headers: list = None) -> None:
		"""
		Запись данных в файл CSV. Получает список вакансий и записывает их в CSV-файл.

		"""

		with open(self.path, 'r', encoding='utf-8') as fp:
			reader = csv.reader(fp, dialect='excel', delimiter=';')

			headers = []
			for header in user_headers:
				if header not in self.headers:
					raise ValueError(f'Недопустимый параметр: {header}\nДопустимые: {self.headers}')
				headers.append(header)

			headers_index = [self.headers.index(header) for header in headers]

			for i, row in enumerate(reader):
				if len(row) < 1 or i == 0:
					continue

				row_to_print = []

				for idx in headers_index:
					row_to_print.append(row[idx])

				print(row_to_print)

	def delete(self) -> None:
		"""
		Удаление файла
		"""

		os.remove(self.path)
		print(f'Файл {self.path} удалён')
