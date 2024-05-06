from telebot import TeleBot
from telebot.types import Message
from telebot.custom_filters import TextMatchFilter
import game
import tele_view
import presenter

bot = TeleBot(token='7128751576:AAEAQJX6eyIhy-b1_vu-zdkGDr2I-2DGOQU')



@bot.message_handler(content_types=['text'])
def get_name(message: Message):
    game = presenter.Presenter(bot, message)
    game.get_text(message)



bot.infinity_polling()

