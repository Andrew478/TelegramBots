import telebot
import time

# Создаём экземпляр бота
bot = telebot.TeleBot('yourtoken')
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '@адрес_канала'

# Загружаем список шуток
f = open('data/adecdotes.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

# Посылаем шутки в телеграм-канал, пока они не закончатся
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(3600)

bot.send_message(CHANNEL_NAME, "Анекдоты закончились :(")
