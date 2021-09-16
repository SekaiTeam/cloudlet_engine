import os, re

from ast import literal_eval
from typing import Any, Optional
from django.conf import settings


class Environ:

	def __init__(self, name: str) -> None:
		self.__var_name = name
		self.__var_meaning: Any = None

	def __converting(self, text: str) -> Any:
		self.__var_meaning: Optional[str] = text

		try:
			self.__var_meaning = literal_eval(self.__var_meaning)
		except SyntaxError:
			self.__var_meaning = None
		except ValueError:
			pass

		return self.__var_meaning

	def set(self, meaning: str) -> None:
		os.environ[self.__var_name] = meaning

	def get(self) -> Any:
		return self.__converting(os.environ[self.__var_name])

	@staticmethod
	def load() -> None:
		parameters = None
		with open(f"{settings.BASE_DIR}/.env", "r") as file:
			parameters = file.readlines()

		if not parameters:
			raise Exception("You definitely created it .env file?")

		for parameter in parameters:
			if result := re.match(r"^(\w+) = (@?.+)$", parameter):
				Environ(result.group(1)).set(result.group(2))
