#!/usr/bin/python
# -*- coding: utf-8 -*-

import cachet
import telebot
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = telebot.TeleBot(BOT_TOKEN)

START_MESSAGE = """
Welcome to the ICON Status Bot

Available commands:
/incidents -> Shows 
"""

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, START_MESSAGE)


@bot.message_handler(commands=['incidents'])
def show_incidents(message):
    incidents = cachet.get_incidents()
    bot.send_message(message.chat.id, 'The following incidents are currently logged in the system:')
    for item in incidents:
        if item['status'] < 4:
            answer = '- %s (%s)' % (item['name'], item['human_status'])

            if item['component'] is not None:
                answer += '\n  _Issue with: %s_' % item['component']['name']

            bot.send_message(message.chat.id, answer, parse_mode='Markdown')

print('Bot started')

bot.polling()
