import os
import json
import locale

from vacancy_parser import VacancyParser


class JSONFileManager:
	"""
	Работа в формате JSON
	"""

	path = './result.json'
	headers = ['name', 'url', 'salary_from', 'salary_to', 'requirements']

	def __init__(self, path: str = None):
		"""
		Инициализации объекта класса.

		:param path:
		"""

		if path:
			self.path = path

	def load_to(self, vacancies: list[VacancyParser], fp: str = None) -> None:
		"""
		Сохранение данных в файл JSON

		:param vacancies:
		:param fp:
		:return:
		"""

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

	def load_from(self, user_headers: list = None) -> None:
		

		headers = []
		result = []
		for header in user_headers:
			if header not in self.headers:
				raise ValueError(f'Недопустимый параметр: {header}\nДопустимые: {self.headers}')
			headers.append(header)

		headers_index = [self.headers.index(header) for header in headers]

		with open(self.path, 'r', encoding='utf-8') as fp:
			data = json.load(fp)
			for value in data.values():
				row = []
				for idx in headers_index:
					row.append(value[idx])
				result.append(row)

		for row in result:
			print(row)

	def delete(self) -> None:
		"""
		Удаление файла

		:return:
		"""

		os.remove(self.path)
		print(f'Файл {self.path} удалён')
