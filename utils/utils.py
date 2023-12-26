from requests import get
from random import shuffle


def load_random_word(url) -> tuple:
    """
    Загружает с сайта www.jsonkeeper.com json список, перемешивает и возвращает
    два значения: слово и его подслова
    :param url: Str
    :return: Str, List
    """
    list_ = get(url).json()
    shuffle(list_)
    return list_[0]['word'], list_[0]['sub_words']
