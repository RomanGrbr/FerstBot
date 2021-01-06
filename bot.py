import telebot


bot = telebot.TeleBot(TOKEN)

# Кнопки
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

# Ответы на команды
@bot.message_handler(commands=['stop'])
def stop_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /stop')

# Ответы на сообщения
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

# Стикер
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True)