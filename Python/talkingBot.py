import fuzzywuzzy
import telebot
import os
from fuzzywuzzy import fuzz

# Создаём бота, пишем свой токен
bot = telebot.TeleBot('yourtoken')

# Загружаем список фраз и ответов в массив
mas = []
if os.path.exists('data/talkingBot.txt'):
    f = open('data/talkingBot.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()

# Находим самую похожую фразу в качестве вопроса и выдаём в качестве ответа следующий элемент списка.
# Используем библиотеку fuzzywuzzy
def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('data/talkingBot.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if(aa > a and aa != a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'

# Команда "Старт"
@bot.message_handler(content_types=["text"])
def handle_text(message):
    s = answer(message.text)
    bot.send_message(message.chat.id, s)

# Запускаем бота
bot.polling(none_stop = True, interval = 0)
