from telebot import TeleBot
from telebot.types import Message
from telebot.custom_filters import TextMatchFilter
import game
import tele_view


class Presenter:
    def __init__(self, bot, message: Message):
        self.game = game.Game(message.from_user.first_name)
        self.telegram_bot = tele_view
        self.bot = bot

    def get_text(self, message: Message):
        if message.text == '/start':
            start_text = self.game.print_pretty_start(message.from_user.first_name)
            self.telegram_bot.send_message_telegram(message, start_text, self.bot)
        elif message.text in ('0', '1', '2', '3', '4'):
            self.game.choosing_human(message.text)
            self.game.choosing_computer()
            result = self.game.determining_winner()
            end_text = self.game.print_pretty_end(result)
            self.telegram_bot.send_message_telegram(message, end_text, self.bot)
        else:
            self.telegram_bot.send_message_telegram(message, 'отсечено', self.bot)









