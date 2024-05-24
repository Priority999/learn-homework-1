"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem 
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    text = '''Привет!\n
    Для тебя доступны следующие команды:
    /planet Mercury - Чтобы узнать, в каком созвездии находится планета Меркурий
    /planet Venus - Чтобы узнать, в каком созвездии находится планета Венера
    /planet Jupiter - Чтобы узнать, в каком созвездии находится планета Юпитер
    /planet Saturn - Чтобы узнать, в каком созвездии находится планета Сатурн
    /planet Uranus - Чтобы узнать, в каком созвездии находится планета Уран
    /planet Neptune - Чтобы узнать, в каком созвездии находится планета Нептун
    /planet Pluto - Чтобы узнать, в каком созвездии находится карликовая планета Плутон
    '''
    print(text)
    update.message.reply_text(text)
    
today = datetime.now()

def constellation(update, context):
    try:
      text_user = update.message.text.split()[1]
      if text_user == 'Mercury':
        mercury = ephem.Mercury()
        mercury.compute(today)
        constellation_mer = ephem.constellation(mercury)
        update.message.reply_text(f'Планета Меркурий находится в созвездии: {constellation_mer}')
      elif text_user == 'Venus':
        venus = ephem.Venus()
        venus.compute(today)
        constellation_v = ephem.constellation(venus)
        update.message.reply_text(f'Планета Венера находится в созвездии: {constellation_v}')
      elif text_user == 'Mars':
        mars = ephem.Mars()
        mars.compute(today)
        constellation_m = ephem.constellation(mars)
        update.message.reply_text(f'Планета Марс находится в созвездии: {constellation_m}')
      elif text_user == 'Jupiter':
        jupiter = ephem.Jupiter()
        jupiter.compute(today)
        constellation_j = ephem.constellation(jupiter)
        update.message.reply_text(f'Планета Юпитер находится в созвездии: {constellation_j}')
      elif text_user == 'Saturn':
        saturn = ephem.Saturn()
        saturn.compute(today)
        constellation_s = ephem.constellation(saturn)
        update.message.reply_text(f'Планета Сатурн находится в созвездии: {constellation_s}')
      elif text_user == 'Uranus':
        uranus = ephem.Uranus()
        uranus.compute(today)
        constellation_u = ephem.constellation(uranus)
        update.message.reply_text(f'Планета Уран находится в созвездии: {constellation_u}')
      elif text_user == 'Neptune':
        neptune = ephem.Neptune()
        neptune.compute(today)
        constellation_n = ephem.constellation(neptune)
        update.message.reply_text(f'Планета Нептун находится в созвездии: {constellation_n}')
      elif text_user == 'Pluto':
        pluto = ephem.Pluto()
        pluto.compute(today)
        constellation_p = ephem.constellation(pluto)
        update.message.reply_text(f'Карликовая планета Плутон находится в созвездии: {constellation_p}')
      else:
        update.message.reply_text(f'Я не знаю такой планеты "{text_user}", попробуй еще раз')
        return
    except IndexError:
        return

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def main():
    mybot = Updater("TOKEN",  use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
