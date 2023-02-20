import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = ''

def start(update, context):
    keyboard = [[InlineKeyboardButton("Перейти на сайт", url='http://www.example.com')],
                [InlineKeyboardButton("Связаться с менеджером по ссылке", url='https://t.me/your_customer_service_bot')]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Здравствуйте! Спасибо за то, что выбрали нашу тур компанию.' 
        'Мы готовы предложить Вам лучшие услуги и помочь организовать незабываемый отдых.'
        'Если у Вас есть какие-либо вопросы или нужна помощь,'
        'для этого нажмите на кнопку ниже ⬇️', reply_markup=reply_markup\
            )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
