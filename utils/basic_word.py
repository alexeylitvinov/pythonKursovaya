class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f'word ("{self.word}", subwords ("{self.subwords}")'

    def start_game(self) -> str:
        """
        Вывод начала игры
        :return: Str
        """
        return f"""Составьте {self.get_count_of_subwords()} слов из слова - "{self.word}"
Слова должны быть не короче 3 букв
Чтобы закончить игру, угадайте все слова или напишите "stop / стоп"
Поехали, ваше первое слово?:"""

    def check_user_response(self, user_answer) -> bool:
        """
        Проверка введенного слова в списке допустимых подслов.
        :return: Bool
        """
        if user_answer in self.subwords:
            return True
        return False

    def get_count_of_subwords(self) -> int:
        """
        Подсчет количества подслов.
        :return: Int
        """
        return len(self.subwords)

    def del_word(self, user_word) -> list:
        """
        Удаление правильного слова пользователя из списка подслов
        :param user_word: Str
        :return: List
        """
        self.subwords.remove(user_word)
