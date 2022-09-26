import telebot

# Создаём экземпляр бота
bot = telebot.TeleBot('5564506581:AAEIZfBSqLnm5rZHaT9LBoKKG_PRk0FzGUs')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я бот, я на связи. Напиши мне что-нибудь.')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

# Запускаем бота
bot.polling(none_stop=True, interval = 0)