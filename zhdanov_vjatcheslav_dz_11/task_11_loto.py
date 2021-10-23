import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._number_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._strikethrough_count = 0

        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        # [' ', ' ', ' ', ' ', 9, 5, 12, 65, 4]

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)
        # [' ', ' ', ' ', 9, 5, 12, 65,' ',  4]
        # [' ', 4, ' ', 5, 9, ' ', 12, ' ',  ' ']

    def __str__(self):
        return f"{self.player_type}:\n{'-' * 26}\n" + \
               '\n'.join([' '.join([str(i).ljust(2) for i in el]) for el in self._card]) + f"\n{'-' * 26}"


class WorldGame:
    def __init__(self, player_card, npc_card):
        self.player_card = player_card
        self.npc_card = npc_card
        self._MAX_ROUNDS = 90
        self.number_round = 0

    def _print_cards(self):
        print(self.player_card)
        print(self.npc_card)

    def _check_value(self, value, card):
        check = False
        for el in card._card:
            if value in el:
                check = True
        return check

    def _strikethrough(self, value, card):
        for el in card._card:
            if value in el:
                el[el.index(value)] = '-'
                card._strikethrough_count = card._strikethrough_count + 1

    def _game_over(self, card, why):
        print(f'{card.player_type} проиграл!')
        print(why)
        return exit()

    def _game_win(self, card):
        if card._strikethrough_count == 15:
            print(f'{card.player_type} победил!')
            return exit()

    def play(self):
        round_value = random.sample(range(1, self._MAX_ROUNDS + 1), self._MAX_ROUNDS)
        for idx, value in enumerate(round_value, 1):
            print(f'Новый бочонок: {value} (осталось {self._MAX_ROUNDS - idx})')
            self._print_cards()
            print('Зачеркнуть цифру? (y/n)')
            player_input = input()
            if player_input == 'n':
                if self._check_value(value, self.player_card):
                    self._game_over(self.player_card, 'Число было на карте')
            elif player_input == 'y':
                if self._check_value(value, self.player_card):
                    self._strikethrough(value, self.player_card)
                else:
                    self._game_over(self.player_card, 'Число отсудсвует на карте')
            else:
                self._game_over(self.player_card, 'Неверный ввод')
            self._strikethrough(value, self.player_card)
            self._game_win(self.player_card)
            self._strikethrough(value, self.npc_card)
            self._game_win(self.npc_card)


player1 = LotoCard('Игрок')
player2 = LotoCard('Компьютер')
play = WorldGame(player1, player2)
play.play()
