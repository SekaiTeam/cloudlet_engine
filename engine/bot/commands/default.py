from engine.bot import handler
from engine.models import Account
from engine.bot.Message import Message


async def start_message(msg: Message, user: Account) -> None:
	await msg("Welcome to CloudletEngine!")


@handler.payload(name = "start")
async def _(msg: Message, user: Account) -> None:
	await start_message(msg, user)

@handler.message(name = "start")
async def _(msg: Message, user: Account) -> None:
	await start_message(msg, user)