from tabulate import tabulate

from parcers.hh_parser import HeadHunterAPI
from parcers.superjob_parser import SuperJobAPI
from managers.csv_manager import CSVFileManager
from managers.json_manager import JSONFileManager


def console_manager() -> None:
	"""
	doc

	:return:
	"""
	menu = 'Меню:' \
		   '\n 1 - Вакансий из HH' \
		   '\n 2 - Ваканский из SuperJob'

	print(menu)
	user_enter = int(input('Введите номер необходимой операции\n\t>> '))

	if user_enter == 1:
		api = HeadHunterAPI()
	elif user_enter == 2:
		api_key = 'v3.r.129465934.5e3b33d356e8a78d8bcfb17b1b458c78ece00fdd.a2eb0cc4fe4b77c6fcfbcb10e64fe935e4fb52c1'
		api = SuperJobAPI(api_key)
	else:
		raise ValueError('Недопустимый ввод')

	user_enter = input('Введите ключевое слово для вакансии\n\t>> ')

	items = api.get_vacancies(user_enter)
	if len(items) < 1:
		print('Не найдено ни одной подходящей вакансии. Повторите попытку')
		return
	vacs = api.convert_vacancies(items)

	menu = 'Собрал вакансии. Выберите следующий шаг:' \
		   '\n 1 - Вывести вакансии без сортировки' \
		   '\n 2 - Отсортировать вакансии по зарплате'
	print(menu)
	user_enter = int(input('Введите номер необходимой операции\n\t>> '))

	if user_enter == 1:
		pass
	elif user_enter == 2:
		vacs.sort(key=lambda vac: vac)
	else:
		raise ValueError('Недопустимый ввод')

	menu = 'Сделано. Выберите следующий шаг:' \
		   '\n 1 - Вывести в консоль без сохранения' \
		   '\n 2 - Сохранить вакансии в CSV' \
		   '\n 3 - Сохранить вакансии в JSON'
	print(menu)
	user_enter = int(input('Введите номер необходимой операции\n\t>> '))
	if user_enter == 1:
		headers = ['name', 'url', 'salary_from', 'salary_to', 'requirements']
		rows = []
		for vac in vacs:
			rows.append([vac.name, vac.url, vac.salary_from, vac.salary_to, vac.requirement])
		table = tabulate(rows, headers)
		print(table)
	elif user_enter == 2:
		fm = CSVFileManager()
		fm.load_to(vacs)
		print(f'Сохранено по пути {fm.path}')
	elif user_enter == 3:
		fm = JSONFileManager()
		fm.load_to(vacs)
		print(f'Сохранено по пути {fm.path}')
	else:
		raise ValueError('Недопустимый ввод')


if __name__ == '__main__':
	console_manager()
