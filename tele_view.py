from telebot import TeleBot
from telebot.types import Message
from telebot.custom_filters import TextMatchFilter


bot = TeleBot(token='7128751576:AAEAQJX6eyIhy-b1_vu-zdkGDr2I-2DGOQU')


# def get_number_gesture(bot):
#     @bot.message_handler(text=['0', '1', '2', '3', '4'])
#     def gesture(message: Message):
#         data.text = message.text



#def send_message_telegram(message, text, bot):
@bot.message_handler()
def send_message_telegram(message, text, bot):
    bot.send_message(message.chat.id, text)


def ip(bot):
    bot.infinity_polling()
