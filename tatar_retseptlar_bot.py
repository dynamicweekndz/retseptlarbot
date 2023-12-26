#Идентификация

import telebot

bot = telebot.TeleBot("6769497405:AAEc_LDTv6eX2BP1E8R0RurIGCRe8EGkOCE")

#Команда приветствия

@bot.message_handler(commands=['rahim_itegez'])
def rahim_itegez(message):
	greeting = f'<b>Рәхим итегез, {message.from_user.first_name}! Я знал, что рано или поздно ты найдешь меня..!</b>'
	bot.send_message(message.chat.id, greeting, parse_mode="html")

#Команда помощи

@bot.message_handler(commands=['help_me'])
def help_me(message):
	otvet = '<b>Чтобы увидеть список доступных рецептов, выбери команду retseptlar! После этого (отдельным!) сообщением впиши название выбранного рецепта :)</b>'
	bot.send_message(message.chat.id, otvet, parse_mode="html")

#Команда retseptlar
@bot.message_handler(commands=['retseptlar'])
def retseptlar(message):
	dict_retsept = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/retseptlar.txt", "rb")
	bot.send_message(message.chat.id, dict_retsept.read(), parse_mode="html")

#Рецепты и фото

@bot.message_handler()
def getting_user_text(message):

	if message.text == "Чак-Чак":
		chakchak_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/chakchak.jpg", "rb")
		chakchak_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/chakchak_r.txt", "rb")
		bot.send_photo(message.chat.id, chakchak_ph)
		bot.send_message(message.chat.id, chakchak_re.read(), parse_mode="html")

	elif message.text == "Азу":
		azu_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/azu.jpg", "rb")
		azu_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/azu_r.txt", "rb")
		bot.send_photo(message.chat.id, azu_ph)
		bot.send_message(message.chat.id, azu_re.read(), parse_mode="html")

	elif message.text == "Бармак":
		barmak_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/barmak.jpg", "rb")
		barmak_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/barmak_r.txt", "rb")
		bot.send_photo(message.chat.id, barmak_ph)
		bot.send_message(message.chat.id, barmak_re.read(), parse_mode="html")

	elif message.text == "Бешбармак":
		beshbarmak_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/beshbarmak.jpg", "rb")
		beshbarmak_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/beshbarmak_r.txt", "rb")
		bot.send_photo(message.chat.id, beshbarmak_ph)
		bot.send_message(message.chat.id, beshbarmak_re.read(), parse_mode="html")

	elif message.text == "Эчпочмак":
		echpochmak_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/echpochmak.jpg", "rb")
		echpochmak_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/echpochmak_r.txt", "rb")
		bot.send_photo(message.chat.id, echpochmak_ph)
		bot.send_message(message.chat.id, echpochmak_re.read(), parse_mode="html")

	elif message.text == "Элеш":
		elesh_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/elesh.jpg", "rb")
		elesh_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/elesh_r.txt", "rb")
		bot.send_photo(message.chat.id, elesh_ph)
		bot.send_message(message.chat.id, elesh_re.read(), parse_mode="html")

	elif message.text == "Губадия":
		gubadiya_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/gubadiya.jpg", "rb")
		gubadiya_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/gubadiya_r.txt", "rb")
		bot.send_photo(message.chat.id, gubadiya_ph)
		bot.send_message(message.chat.id, gubadiya_re.read(), parse_mode="html")

	elif message.text == "Кыстыбый":
		kistibiy_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/kistibiy.jpg", "rb")
		kistibiy_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/kistibiy_r.txt", "rb")
		bot.send_photo(message.chat.id, kistibiy_ph)
		bot.send_message(message.chat.id, kistibiy_re.read(), parse_mode="html")

	elif message.text == "Кыздырма":
		kizdirma_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/kizdirma.jpg", "rb")
		kizdirma_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/kizdirma_r.txt", "rb")
		bot.send_photo(message.chat.id, kizdirma_ph)
		bot.send_message(message.chat.id, kizdirma_re.read(), parse_mode="html")

	elif message.text == "Кош теле":
		koshtele_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/koshtele.jpg", "rb")
		koshtele_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/koshtele_r.txt", "rb")
		bot.send_photo(message.chat.id, koshtele_ph)
		bot.send_message(message.chat.id, koshtele_re.read(), parse_mode="html")

	elif message.text == "Коймак":
		koymak_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/koymak.jpg", "rb")
		koymak_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/koymak_r.txt", "rb")
		bot.send_photo(message.chat.id, koymak_ph)
		bot.send_message(message.chat.id, koymak_re.read(), parse_mode="html")

	elif message.text == "Куллама":
		kullama_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/kullama.jpg", "rb")
		kullama_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/kullama_r.txt", "rb")
		bot.send_photo(message.chat.id, kullama_ph)
		bot.send_message(message.chat.id, kullama_re.read(), parse_mode="html")

	elif message.text == "Манты":
		manti_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/manti.jpg", "rb")
		manti_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/manti_r.txt", "rb")
		bot.send_photo(message.chat.id, manti_ph)
		bot.send_message(message.chat.id, manti_re.read(), parse_mode="html")

	elif message.text == "Пахлава":
		pahlava_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/pahlava.jpeg", "rb")
		pahlava_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/pahlava_r.txt", "rb")
		bot.send_photo(message.chat.id, pahlava_ph)
		bot.send_message(message.chat.id, pahlava_re.read(), parse_mode="html")

	elif message.text == "Плов":
		plov_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/plov.jpeg", "rb")
		plov_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/plov_r.txt", "rb")
		bot.send_photo(message.chat.id, plov_ph)
		bot.send_message(message.chat.id, plov_re.read(), parse_mode="html")

	elif message.text == "Салма":
		salma_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/salma.jpg", "rb")
		salma_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/salma_r.txt", "rb")
		bot.send_photo(message.chat.id, salma_ph)
		bot.send_message(message.chat.id, salma_re.read(), parse_mode="html")

	elif message.text == "Салма":
		salma_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/salma.jpg", "rb")
		salma_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/salma_r.txt", "rb")
		bot.send_photo(message.chat.id, salma_ph)
		bot.send_message(message.chat.id, salma_re.read(), parse_mode="html")

	elif message.text == "Шурпа":
		shurpa_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/shurpa.jpg", "rb")
		shurpa_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/shurpa_r.txt", "rb")
		bot.send_photo(message.chat.id, shurpa_ph)
		bot.send_message(message.chat.id, shurpa_re.read(), parse_mode="html")

	elif message.text == "Талкыш калеве":
		talkishkaleve_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/talkishkaleve.jpg", "rb")
		talkishkaleve_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/talkishkaleve_r.txt", "rb")
		bot.send_photo(message.chat.id, talkishkaleve_ph)
		bot.send_message(message.chat.id, talkishkaleve_re.read(), parse_mode="html")

	elif message.text == "Токмач":
		tokmach_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/tokmach.jpg", "rb")
		tokmach_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/tokmach_r.txt", "rb")
		bot.send_photo(message.chat.id, tokmach_ph)
		bot.send_message(message.chat.id, tokmach_re.read(), parse_mode="html")

	elif message.text == "Тулма":
		tulma_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/tulma.jpg", "rb")
		tulma_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/tulma_r.txt", "rb")
		bot.send_photo(message.chat.id, tulma_ph)
		bot.send_message(message.chat.id, tulma_re.read(), parse_mode="html")

	elif message.text == "Зур белиш":
		zurbelish_ph = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/zurbelish.jpg", "rb")
		zurbelish_re = open("C:/Users/Livas/AppData/Local/Microsoft/WindowsApps/bot/zurbelish_r.txt", "rb")
		bot.send_photo(message.chat.id, zurbelish_ph)
		bot.send_message(message.chat.id, zurbelish_re.read(), parse_mode="html")



bot.polling(none_stop=True)
