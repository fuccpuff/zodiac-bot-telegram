# -*- coding: utf-8 -*-

import telebot
import random
import config
from telebot import types

bot = telebot.TeleBot(config.token)

# Заготовки для трёх предложений
first = ['Сегодня - идеальный день для новых начинаний',
         'Оптимальный день для того, чтобы решиться на смелый поступок',
         'Будьте осторожны, сегодня звёзды не повлияют на ваше финансовое состояние',
         'Лучшее время для того, чтобы начинать новые отношения или разбораться со старыми',
         'Плодотворный день для того, чтобы разобраться с накопившимися делами.']
second = ['Но помните, что даже в этом случае нужно не забывать про',
          'Если поедете за город, заранее подумайте про',
          'Те, кто сегодня нацелен выполнить множество дел, должны помнить про',
          'Если у вас упадок сил, обратите внимание на',
          'Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про']
second_add = ['отношения с друзьями и близкими.',
              'работу и деловые вопросы, которые могут так некстати помешать планам',
              'себя и своё здоровье, иначе к вечеру возможен полный раздрай',
              'бытовые вопросы - особенно те, которые вы не доделали вчера',
              'отдых, чтобы не превратить себя в загнанную лошадь в конце месяца']
third = ['Злые языки могут говорить вам обратное, но сегодня их слушать не нужно',
         'Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.',
         'Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца',
         'Не нужно бояться одиноких встреч - сегодня то самое время, когда они значат многое',
         'Если встретите незнакомца на пути - проявите участие, и тогда эта встреча посулит вам приятные хлопоты']

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали привет
    if message.text == 'Привет':
        # Пишем приветствие
        bot.send_message(message.from_user.id, 'Привет, сейчас покажу тебе гороскоп на сегодня')
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        # Овен
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        # Добавляем кнопку Овен на экран
        keyboard.add(key_oven)
        # Телец
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        # Близнецы
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        # Рак
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        # Лев
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        # Дева
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        # Весы
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        # Скорпион
        key_skorp = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_skorp)
        # Стрелец
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        # Козерог
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        # Водолей
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        # Рыбы
        key_rybi = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_rybi)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message (message.from_user.id, 'Я тебя не понимаю, напиши /help')

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок - выводим гороскоп
    if call.data == 'zodiac':
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем гороскоп юзеру
        bot.send_message(call.message.chat.id, msg)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, это твой первый бот в Telegram ❤️', reply_markup=keyboard)


# @bot.message_handler(content_types=['text'])
# def send_text(message):
#    if message.text.lower() == 'привет':
#        bot.send_message(message.chat.id, 'Привет, мой создатель!')
#    elif message.text.lower() == 'пока':
#        bot.send_message(message.chat.id, 'Прощай, создатель')
#    elif message.text.lower() == 'я тебя люблю':
#        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

if __name__ == '__main__':
    bot.polling(none_stop=True)

