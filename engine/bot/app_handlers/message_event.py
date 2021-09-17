from engine.bot.vk.LongPoll import api as API
from engine.models import Account
from engine.bot.Message import Message
from engine.bot import handler as Handler
from engine.bot.engine_message import command_not_found_message


async def message_event(
						item: dict,
						api: API,
						lor: Account,
						msg: Message,
						handler: Handler,
					) -> None:

	data = await api("users.get", {"user_ids": item['object']['user_id']})
	user = lor(data['response'][0])
	callback_command = item['object']['payload']['button'].split()
	msg.path_args = callback_command

	for command in handler.callback_commands:
		if (command.name in ['', callback_command[0]]) and (command.dialog == user.dialog or command.dialog == "all"):
			command.handle(msg, user)
			break
	else:
		if item['object']['message']['peer_id'] < 2000000000:
			await command_not_found_message(msg, user)
