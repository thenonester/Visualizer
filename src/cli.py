"""CLI - Приложение для визуализации графа зависимостей"""

import sys\

def parse(argv):
	"""Разбирает аргументы командной строки"""
	args = {"Package": None, "Source": None, "test": False, "Depth": None, "Filter": None}
	i=0
	while i < len(argv):
		token = argv[i]
		if token == "--package":
			args["Package"] = value(argv, i)
			i+=2
		elif token == "--source":
			args["Source"] = value(argv, i)
			i+=2
		elif token == "--test":
			args["Test"] = True
			i+=1
		elif token == "--depth":
			args["Depth"] = dep(value(argv, i))
			i+=2
		elif token == "--filter":
			args["Filter"] = value(argv, i)
			i+=2
		else:
			raise ValueError(f"Unknown argument {token}")
	return args

def value(argv, i):
	"""возвращает значение после флага"""
	if i+1 >= len(argv):
		raise ValueError(f"{argv[i]} requires a value")
	return argv[i+1]

def dep(val):
	"""преобразование строки в число"""
	try:
		depth = int(val)
	except ValueError:
		raise ValueError(f"depth must be integer: {val}")
	if depth <= 0:
		raise ValueError(f"depth must be positive: {val}")
	return depth

def valid(args):
	"""Проверка наличие параметров"""
	if not args["Package"]:
		raise ValueError("--package required")
	if not args["Source"]:
		raise ValueError("--source required")
	if args["Package"] == None:
		raise ValueError("--package requires argument")
	if args["Package"] == None:
		raise ValueError("--package requires argument")

def printt(args):
	"""Вывод параметров, настраиваемых пользователем"""
	print("="*40)
	print(f"	package:	{args["Package"]}")
	print(f"	source:		{args["Source"]}")
	print(f"	test:		{args["Test"]}")
	print(f"	depth:		{args["Depth"]}")
	print(f"	filter:		{args["Filter"]}")
	print("="*40)

def main():
	"""Вход в приложение"""
	try:
		args = parse(sys.argv[1:])
		valid(args)
	except ValueError as e:
		print(f"Error: {e}")
		sys.exit(1)
	printt(args)

if __name__ == "__main__":
	main()
