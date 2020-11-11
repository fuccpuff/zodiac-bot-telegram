import logging
import re
import threading
from datetime import datetime, time, timedelta
from time import sleep

import telebot
from telebot import types
import config


bot = telebot.AsyncTeleBot(config.token)


commands = { # Описание команд использующиеся в команде /help
    'start': 'Стартовое сообщение и предложение зарегистрироваться',
    'help': 'Информация о боте и список доступных команд',
    'registration': 'Выбор учебного заведения, выбор факультета и группы для вывода информации',
    'send_report': 'Отправка обратной связи',
    'auto_posting_on <ЧЧ:ММ>': 'Подписка на автоматическую рассылку расписания',
    'auto_posting_off': 'Выключение автоматической отправки расписания'
}

# Создаем клавиатуру на все дни
def get_date_keyboard():
    date_select = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    date_select.row('Сегодня')
    date_select.row('Вся неделя')
    date_select.row('Понедельник', 'Вторник')
    date_select.row('Среда', 'Четверг')
    date_select.row('Пятница', 'Суббота')

    return date_select

# Команда /registration
#@bot.message_handler(commands=['registration'])
#def command_registration(m):
#    registration('reg:stage 1:none', m.chat.id, m.chat.first_name, m.chat.username)


# хелп страница
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = 'Доступны следующие команды \n'
    for key in commands:
        help_text += '/' + key + ': '
        help_text += commands[key] + '\n'
    bot.send_message(cid, help_text, reply_markup=get_date_keyboard())

    help_text = ('Описание кнопок: \nКнопка "Сегодня" выводит расписание на сегодняшний день, '
                 'причем с учётом типа недели (числитель/знаменатель), но есть один нюанс: если сегодня воскресенье'
                 'или время больше, чем 19:00, то выводится расписание на следующий день\n')
    bot.send_message(cid, help_text, reply_markup=get_date_keyboard())
    guide_url = "@fuccbwoi"
    help_text = 'Более подробную инструкцию и помощь вы сможете узнать написав мне: {}'.format(guide_url)
    bot.send_message(cid, help_text, reply_markup=get_date_keyboard())

bot.polling(none_stop=True)