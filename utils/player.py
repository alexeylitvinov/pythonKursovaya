class Player:
    def __init__(self, name):
        self.name = name
        self.user_input_words = []

    def __repr__(self):
        return f'Player("{self.name}")'

    def get_count_user_words(self) -> int:
        """
        Получение количества использованных слов.
        :return: Int
        """
        return len(self.user_input_words)

    def append_user_words(self, word):
        """
        Добавление слова в использованные слова.
        :param word: Str
        :return:
        """
        self.user_input_words.append(word)

    def check_word_used(self, word) -> bool:
        """
        Проверка использования данного слова до этого.
        :param word: Str
        :return:Bool
        """
        if word in self.user_input_words:
            return True
        return False

    def end_game(self) -> str:
        """
        Выводит результаты игры
        :return: Str
        """
        return f'\nИгра завершена, вы {self.name} угадали {self.get_count_user_words()} слов!'
