import telebot

bot = telebot.Telebot('5777308232:AAFsfWJAW2KV7Isr69m64XUwmrUFyadqtk4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Вахуи, не высирай пж</b>', parse_mode='html')

bot.polling(none_stop=True)