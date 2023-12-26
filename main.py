from utils.utils import load_random_word
from utils.basic_word import BasicWord
from utils.player import Player

URL = 'https://api.jsonserve.com/KNtoDx'


def main():
    print('Введите имя игрока:')
    player = Player(input())
    print(f'Привет, {player.name}')
    game = BasicWord(*load_random_word(URL))
    print(game.start_game())
    while len(game.subwords) != 0:
        player_input = input().lower()
        if player_input == 'stop' or player_input == 'стоп':
            break
        if player.check_word_used(player_input):
            print('уже использовано')
        elif not game.check_user_response(player_input):
            print('неверно')
        else:
            player.append_user_words(player_input)
            game.del_word(player_input)
            print(f'верно, еще {len(game.subwords)} слов ')

    print(player.end_game())


if __name__ == '__main__':
    main()
