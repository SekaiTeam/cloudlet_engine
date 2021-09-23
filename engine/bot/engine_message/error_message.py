from engine.models import Account
from engine.bot.Message import Message
from utils import console


async def error_message(msg: Message, user: Account, ex: str = None, error: list = None) -> None:
	"""function for sending an error message"""
	error = '\n'.join(error)
	console.error(f"{ex}\n{error}")
	await msg('❌ Произошла ошибка, попробуйте чуть позже', reply_to=msg.id)