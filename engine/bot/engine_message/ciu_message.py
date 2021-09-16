from engine.models import Account
from engine.bot.Message import Message

async def chat_invite_user_message(msg: Message, user: Account) -> None:
	"""function for sending a message about adding to a chat"""
	await msg("Спасибо что добавили в беседу 😊")