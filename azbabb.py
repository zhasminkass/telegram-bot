import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Стажировки")
	item2 = types.KeyboardButton("Вакансии")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}\n\n, бот, который поможет тебе найти стажировку, производственную практику. Если ты студент, выпускник бакалавриата и магистратуры, то ты в нужном месте.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Стажировки':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("IT", callback_data='it')
			item2 = types.InlineKeyboardButton("Макркетинг", callback_data='mark')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Какая у тебя специальность?', reply_markup=markup)
		elif message.text == 'Вакансии':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Программист", callback_data='vc_it')
			item2 = types.InlineKeyboardButton("Макркетолог", callback_data='vc_mark')
			

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Выбери профессию', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'it':
				bot.send_message(call.message.chat.id, 'Стажер-программист 1С\n\nот 60 000 KZT до вычета налогов\n\nТребуемый опыт работы: не требуется\n\nСтажировка, полный день')
			elif call.data == 'mark':
				bot.send_message(call.message.chat.id, 'Стажер отдела маркетинга\n\nдо 60 000 KZT до вычета налогов\n\nТребуемый опыт работы: не требуется\n\nСтажировка, полный день')

			if call.data == 'vc_it':
				bot.send_message(call.message.chat.id, 'Технический специалист (IT)\n\nот 200 000 до 300 000 KZT на руки\n\nТребуемый опыт работы: 1–3 года\n\nПолная занятость, сменный график')
			elif call.data == 'vc_mark':
				bot.send_message(call.message.chat.id, 'Контент в отдел Маркетинга\n\nот 100 000 до 200 000 KZT на руки\n\nТребуемый опыт работы: не требуется\n\nПолная занятость, полный день')

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)