'''
класс компа
    - генерация жеста компом(циферкой)
    - из цифр в жесты
класс жесты(просто их перечисление) и взаимосвязи
    - перечисление жестов, взаимосвязи выигрыш, проигрыш.
    - принять жесты, взаимосвязь, вернуть
класс игрок(счет, ввод с клавы)
    - правильность ввода(цифра это цифра)
    - проверить диапазон цифры
    - из цифр в жесты
класс игра(всё)
    поле: счёт
    - красивый вывод(добро пожаловать игрок)
    - класс игрока
    - класс компа
    - класс жесты
    - изменения счета
    - вывод счета и победителя
'''
from random import randint
import unittest
from unittest.mock import patch


class Game:
    _gesture = {
        'Камень': ('Ящерица', 'Ножницы'),
        'Ящерица': ('Спок', 'Бумага'),
        'Бумага': ('Камень', 'Спок'),
        'Спок': ('Камень', 'Ножницы'),
        'Ножницы': ('Бумага', 'Ящерица')
    }

    def __init__(self, name):
        self.gesture_human = None
        self.gesture_comp = None
        self.total = dict.fromkeys(('Компьютер', name), 0)
        self.name = name

    def choosing_computer(self):
        number = randint(0, 4)
        self.gesture_comp = list(self._gesture.keys())[number]

    def choosing_human(self, number_gesture):
        if not number_gesture.isdigit():
            raise TypeError('Нужно ввести >число<!')
        number = int(number_gesture)
        if not 0 <= number <= 4:
            raise ValueError('Нужно ввести число диапазон от 0 до 4')

        self.gesture_human = list(self._gesture.keys())[number]

    def determining_winner(self):
        if self.gesture_comp == self.gesture_human:
            return None
        elif self.gesture_comp in self._gesture[self.gesture_human]:
            return self.name
        return 'Компьютер'

    def calculation(self, winner):
        self.total[winner] += 1

    def print_pretty_start(self, name):
        return f''' Добро пожаловать, {name}, на очередную игру! в «Камень-ножницы-бумага-ящерица-Спок»
                    Выберите, пожалуйста, число от 0 до 4, где 
                    0 - Камень
                    1 - Ящерица
                    2 - Бумага
                    3 - Спок
                    4 - Ножницы
        '''

    def print_pretty_end(self, winner):
        announc = f'Победитель {winner}' if winner else 'Ничья'
        return f'''Игрок выбрал {self.gesture_human},  Компьютер выбрал {self.gesture_comp}
                   Игра завершена:    {announc}   !!!
                   Общий счёт {self.total}'
        '''



class TestIsCorrectEquation(unittest.TestCase):
    def setUp(self):
        self.q = Game('Обь')

    def test_main(self):
        with patch('builtins.input', side_effect=['1']):
            self.assertIsNone(self.q.choosing_human())

    def test_value_error(self):
        with patch('builtins.input', side_effect=['5']):
            with self.assertRaises(ValueError):
                self.q.choosing_human()

    def test_type_error(self):
        with patch('builtins.input', side_effect=['asdf']):
            with self.assertRaises(TypeError):
                self.q.choosing_human()