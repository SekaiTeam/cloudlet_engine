import time
import asyncio, aiohttp, re
import os, importlib, uvloop

from engine.bot import handler
from engine.models import Account
from engine.bot.app_handlers import message_new, message_event
from engine.bot.Message import Message
from engine.bot.vk.LongPoll import LongPoll, api

class VKBot:

	def __init__(self):
		os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
		uvloop.install()
		self.ioloop = asyncio.get_event_loop()
		self.ioloop.run_until_complete(asyncio.wait([self.ioloop.create_task(self.start_bot())]))

	def load_or_create(self, data):
		return Account.objects.get_or_create(user_id=data['id'], defaults={'username': data['first_name']})[0]

	async def start_bot(self):
		Account.TempBot.bot = api
		self.read_handlers()
		self.longpoll = LongPoll()
		await self.longpoll.get_server()
		
		@self.longpoll.event()
		async def _(item):
			if item['type'] == "message_new":
				await message_new(item, api, self.load_or_create, Message(item), handler)
			elif item['type'] == "message_event":
				await message_event(item, api, self.load_or_create, Message(item, True), handler)

		await self.longpoll.update()

	def read_handlers(self):
		for root, dirs, files in os.walk('engine/bot/commands'):
			check_extension = filter(lambda x: x.endswith('.py'), files)
			for command in check_extension:
				path = os.path.join(root, command)
				spec = importlib.util.spec_from_file_location(command, os.path.abspath(path))
				module = importlib.util.module_from_spec(spec)
				spec.loader.exec_module(module)

