from datetime import datetime


def console(text, level):
	time = datetime.now().strftime("%H:%M:%S %m.%d")

	if level == "info":
		level_fmt = "\033[32mINFO\033[0m"
		text_fmt = f"\033[32m{text}\033[0m"
	elif level == "warning":
		level_fmt = "\033[33mWARNING\033[0m"
		text_fmt = f"\033[33m{text}\033[0m"
	elif level == "error":
		level_fmt = "\033[31mERROR\033[0m"
		text_fmt = f"\033[31m{text}\033[0m"

	engine_msg_fmt = f'[\033[36m{time}\033[0m | {level_fmt}] \033[46m[CloudletEnigne]\033[0m {text_fmt}'
	engine_msg = f'[{time} | {level.upper()}] [CloudletEnigne] {text}\n'

	with open("engine.log", "a") as log_file:
		log_file.write(engine_msg)
	print(engine_msg_fmt)


def info(text):
    console(text, "info")


def warning(text):
    console(text, "warning")


def error(text):
    console(text, "error")

