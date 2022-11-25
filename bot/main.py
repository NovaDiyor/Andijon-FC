import requests

# TOKEN = "5498068148:AAGjrSkT6rCy8pLCHE_IqDr5X941D7YTpa0"
# chat_id = "-1001619375200"


def SendMessage(token, chat_id, name, surname, phone_number, address, postal_code, email, region, city):
    result = f"Name: {name},\nSurname: {surname}\nPhone number : {phone_number}\n Address: {address}\nPostal code: {postal_code}\n Email :{email}\n Region: {region}\nCity {city}\n"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={result}"
    work = requests.get(url)





























# import telebot
#
# bot = telebot.TeleBot("5498068148:AAGjrSkT6rCy8pLCHE_IqDr5X941D7YTpa0")
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, 'context')
#
# @bot.message_handler(commands=['order'])
# def send_order(message):
# 	bot.reply_to(message, 'Salom')
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
# bot.infinity_polling()