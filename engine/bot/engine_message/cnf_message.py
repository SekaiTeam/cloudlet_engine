from engine.models import Account
from engine.bot.Message import Message

async def command_not_found_message(msg: Message, user: Account) -> None:
	"""function for sending a message about a command not found"""
	await msg('Команда не найдена, воспользуйтесь кнопками 😔')