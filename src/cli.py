"""CLI - Приложение для визуализации графа зависимостей"""

import sys\

def parse(argv):
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
			args["test"] = True
			i+=1
		elif token == "--depth":
			args["Test"] = value(argv, i)
			i+=2
		elif token == "--filter":
			args["Filter"] = value(argv, i)
			i+=2
		else:
			raise ValueError(f"Unknown argument {token}")
	return args

def value(argv, i):
	if i+1 >= len(argv):
		raise ValueError(f"{argv[i]} requires a value")
	return argv[i+1]

def main():
	"""Вход в приложение"""
	try:
		args = parse(sys.argv[1:])
	except ValueError as e:
		print(f"Error: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
