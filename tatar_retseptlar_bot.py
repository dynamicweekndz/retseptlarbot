import telebot

bot = telebot.TeleBot("6769497405:AAEc_LDTv6eX2BP1E8R0RurIGCRe8EGkOCE")

@bot.message_handler(commands=['salam'])
def salam(message):
	greeting = f'<b>Сәлам, {message.from_user.first_name}! Я знал, что рано или поздно ты придёшь ко мне..!</b>'
	bot.send_message(message.chat.id, greeting, parse_mode="html")

@bot.message_handler()
def getting_user_text(message):
	if message.text == "Чак-чак":
		photo_chack = open(" ", "rb")
		bot.send_photo(message.chat.id, )

bot.polling(none_stop=True)