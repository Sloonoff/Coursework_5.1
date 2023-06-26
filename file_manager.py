import csv
import locale
import os
import json

from vacancy_parser import VacancyParser


class CSVFileManager:
	path = './result.csv'
	headers = ['name', 'url', 'salary_from', 'salary_to', 'requirements']

	def __init__(self, path: str = None):
		if path:
			self.path = path

	def load_to(self, vacancies: list[VacancyParser]):
		with open(self.path, 'w', encoding='utf-8') as fp:
			writer = csv.writer(fp, dialect='excel', delimiter=';')
			writer.writerow(self.headers)

			for vac in vacancies:
				row = [vac.name, vac.url, vac.salary_from, vac.salary_to, vac.requirement]
				print(row)
				writer.writerow(row)

	# print(f'Сохранено по пути {self.path}')

	def load_from(self, *args):
		with open(self.path, 'r', encoding='utf-8') as fp:
			reader = csv.reader(fp, dialect='excel', delimiter=';')

			headers = []
			for els in args:
				for el in els:
					headers.append(el)

			for header in headers:
				if header not in self.headers:
					raise ValueError(f'Недопустимый параметр: {header}\nДопустимые: {self.headers}')

			headers_index = [self.headers.index(header) for header in headers]

			for i, row in enumerate(reader):
				if len(row) < 1 or i == 0:
					continue

				row_to_print = []

				for idx in headers_index:
					row_to_print.append(row[idx])

				print(row_to_print)

	def delete(self):
		os.remove(self.path)
		print(f'Файл {self.path} удалён')


class JSONFileManager:
	path = './result.json'

	def __init__(self, path: str = None):
		if path:
			self.path = path

	def load_to(self, vacancies: list[VacancyParser], fp: str = None) -> None:
		if fp:
			path = fp
		else:
			path = self.path

		data = dict().fromkeys(range(len(vacancies)), [])
		for key in data.keys():
			vacancy = vacancies[key]
			data[key] = [vacancy.name, vacancy.url, vacancy.salary_from, vacancy.salary_to, vacancy.requirement]

		with open(path, 'w', encoding=locale.getpreferredencoding()) as fp:
			json.dump(data, fp, indent=4)

	def delete(self):
		os.remove(self.path)
		print(f'Файл {self.path} удалён')