import os
import json
import locale

from work_sercher.parcers.vacancy_parser import VacancyParser


class JSONFileManager:
	"""
	Работа в формате JSON
	"""

	path = './result.json'

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

	def delete(self) -> None:
		"""
		Удаление файла

		:return:
		"""

		os.remove(self.path)
		print(f'Файл {self.path} удалён')
