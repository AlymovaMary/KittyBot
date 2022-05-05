import requests
import os
from dotenv import load_dotenv
from glob import glob
import random
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup

load_dotenv()

auth_token = os.getenv('TOKEN')
account_sid = os.getenv('ACCOUNT_SID')

URL = 'https://api.thecatapi.com/v1/images/search'

def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        print(error)      
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat

def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Привет, я SimbaBot!')

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
                ['/Simba', '/Dizel'],
                ['/Glasha', '/Aiva'],
                ['/Plusha', '/RandomCat']])
    context.bot.send_message(
        chat_id=chat.id,
        text='Хочешь я покажу тебе котиков, {}!'.format(name),
        reply_markup=buttons  
        )

def simba_cat():
    lists = glob('Simba/*')  # создаем список из названий картинок
    picture = random.choice(lists)  # берем из списка одну картинку
    return picture

def new_simba(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, photo=open(simba_cat(),  'rb'))

def dizel_cat():
    lists = glob('Dizel/*')  # создаем список из названий картинок
    picture = random.choice(lists)  # берем из списка одну картинку
    return picture

def new_dizel(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, photo=open(dizel_cat(),  'rb'))

def plusha_cat():
    lists = glob('Plusha/*')  # создаем список из названий картинок
    picture = random.choice(lists)  # берем из списка одну картинку
    return picture

def new_plusha(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, photo=open(plusha_cat(),  'rb'))

def glasha_cat():
    lists = glob('Glasha/*')  # создаем список из названий картинок
    picture = random.choice(lists)  # берем из списка одну картинку
    return picture

def new_glasha(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, photo=open(glasha_cat(),  'rb'))

def aiva_cat():
    lists = glob('Aiva/*')  # создаем список из названий картинок
    picture = random.choice(lists)  # берем из списка одну картинку
    return picture

def new_aiva(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, photo=open(aiva_cat(),  'rb'))


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())

def main():

    updater = Updater(token=auth_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('RandomCat', new_cat))
    updater.dispatcher.add_handler(CommandHandler('Simba', new_simba))
    updater.dispatcher.add_handler(CommandHandler('Dizel', new_dizel))
    updater.dispatcher.add_handler(CommandHandler('Plusha', new_plusha))
    updater.dispatcher.add_handler(CommandHandler('Glasha', new_glasha))
    updater.dispatcher.add_handler(CommandHandler('Aiva', new_aiva))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling()
    updater.idle() 

if __name__ == '__main__':
    main() 