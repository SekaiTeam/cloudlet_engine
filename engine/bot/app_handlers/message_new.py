import re
from ast import literal_eval as LE
from engine.bot.vk.LongPoll import api as API
from engine.models import Account
from engine.bot.Message import Message
from engine.bot import handler as Handler
from json import loads
from utils import Environ
from engine.bot.engine_message import command_not_found_message, chat_invite_user_message


async def message_new(
						item: dict, 
						api: API,
						lor: Account,
						msg: Message,
						handler: Handler,
					) -> None:

	if item['object']['message']['from_id'] > 1:
		data = await api("users.get", {"user_ids": item['object']['message']['from_id']})
		user = lor(data['response'][0])

		if not item['object']['message'].keys() & {"payload"}:
			if "action" not in item["object"]['message']:

				processed_name = re.sub(r'^[^а-яА-ЯёЁ]\s', '', item['object']['message']['text'].lower().strip())
				processed_name = re.sub(fr'\[club{Environ("GROUP_ID").get()}|@?.+\]\s', '', processed_name)
				processed_name = processed_name.replace("/", "")
				path_args = re.split(r'\s+', processed_name)
				msg.path_args = path_args

				for command in handler.commands:
					if ((not command.with_args and command.name in ['', processed_name]) \
						or (command.with_args and command.name in ['', path_args[0], " ".join(x for x in path_args[0:len(command.name.split())]) if len(path_args) >= len(command.name.split()) else ""])) \
					and (command.dialog == user.dialog or command.dialog == "all"):
						await command.handle(msg, user)
						break
				else:
					if item['object']['message']['peer_id'] < 2000000000:
						await command_not_found_message(msg, user)
			else:
				if item["object"]['message']['action']['type'] == "chat_invite_user":
					await chat_invite_user_message(msg, user)
		else:
			try:
				payload_command = LE(item['object']['message']['payload'])
				if payload_command.keys() & {"command"}:
					if payload_command['command'] == "not_supported_button":
						payload_command = loads(payload_command['payload'])["button"].split()
					else:
						payload_command = payload_command["command"].split()
				else:
					payload_command = payload_command["button"].split()

				msg.path_args = payload_command

				for command in handler.payload_commands:
					if (command.name in ['', payload_command[0]]) and (command.dialog == user.dialog or command.dialog == "all"):
						await command.handle(msg, user)
						break
				else:
					if item['object']['message']['peer_id'] < 2000000000:
						await command_not_found_message(msg, user)
			except Exception as e:
				print(e)