import telebot

bot = telebot.TeleBot('5468943154:AAH9vo6g6n4Ts-9gHOXaKEe3iCtJ3YIjM8c')

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

# Обрабатываются все документы и аудиозаписи.
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

bot.polling(none_stop=True)