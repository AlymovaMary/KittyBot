from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup

updater = Updater(token='5319551654:AAHSis0zie9WyYC1_p1W1xR4t0YQKR2kzJU')

def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Привет, я SimbaBot!')

def wake_up(update, context):
    # В ответ на команду /start 
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
                ['Показать Синдбада Морекота', 'Показать Дизеля'],
                ['Показать Глашу', 'Показать Эйву'],
                ['Показать Плюшу', 'Показать случайного ]
            ])
    context.bot.send_message(
        chat_id=chat.id,
        text='Теперь я буду жить у тебя в телефоне, {}!'.format(name),
        reply_markup=buttons  
        )
updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle() 