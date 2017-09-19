import sys
import time
import telepot
import pyautogui
from telepot.loop import MessageLoop
from tokens import *

class MyBot(telepot.Bot):
	def __init__(self, *args, **kwargs):
		super(MyBot, self).__init__(*args, **kwargs)
		self.answerer = telepot.helper.Answerer(self)
		self._message_with_inline_keyboard = None
		
	def on_chat_message(self, msg):
		content_type, chat_type, chat_id = telepot.glance(msg)
		
		# For debugging and get admin id
		# print(content_type, chat_type, chat_id)
	
		if chat_id in adminId:
			if content_type == 'text':
				if msg['text'] == '/capture':
					bot.sendChatAction(chat_id, 'typing')
					bot.sendMessage(chat_id, "Capturing image")
					self.capture_img()
					bot.sendPhoto(chat_id, photo=open('img\\screenshot.png', 'rb'))
		
		else:
			bot.sendMessage(chat_id, "Not admin")
	def capture_img(self):
		pic = pyautogui.screenshot()
		pic.save('img\\screenshot.png')
		return
	
TOKEN = telegrambot

bot = MyBot(TOKEN)
MessageLoop(bot).run_as_thread()
# Umcomment for debugging
# print('Listening ...')

while 1:
	time.sleep(10)