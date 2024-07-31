import utils
from player import Player

welcome_text = """
欢迎来到野猪游戏！

一、基础流程与获胜条件

两名玩家轮流投掷骰子，每次最多投掷十个，该回合的分数计算参照计分规则，分数首先达到 `GOAL` 的玩家即为获胜（`GOAL` 默认为 100）。

二、计分规则

基本计分规则

- 母猪悲伤：如果任意一个骰子的点数为 1，则当前玩家的回合得分为 1，否则为所有投掷骰子点数的总和。

附加计分规则（可选）

- 野猪乱斗：玩家当前回合可以选择不投掷骰子，不投掷骰子的玩家本回合的计分规则如下：
\t对手分数的十位数与当前玩家的个位数差值绝对值的三倍（如果对手的分数为个位数则十位数为0）。
\t如果计算结果刚好为 0，则获得 1 分。

- 疑神疑鬼：如果本次得分后累计的分数为疑数，那么这个分数则直接增长到下一个素数
\t疑数：如果一个数正好有 3 或 4 个因数，那么称该数字为疑数
"""


class Game(object):
    GOAL = 100

    ENABLE_BOAR_BRAWL = '野猪乱斗'
    ENABLE_SUS_FUSS = '疑神疑鬼'
    OPTIONS = {
        ENABLE_BOAR_BRAWL: False,
        ENABLE_SUS_FUSS: True
    }

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player1.rival = self.player2
        self.player2.rival = self.player1
        self.winner: str = ''
        self.__current_player = self.player2

    def is_over(self):
        if self.player1.win():
            self.winner = self.player1.name
            return True
        elif self.player2.win():
            self.winner = self.player2.name
            return True
        return False

    def next_player_round(self):
        if self.__current_player == self.player1:
            self.__current_player = self.player2
            return self.player2
        else:
            self.__current_player = self.player1
            return self.player1


def is_valid_number(n: int) -> bool:
    if n < 0 or n > 10:
        return False
    if not game.OPTIONS[Game.ENABLE_BOAR_BRAWL] and n == 0:
        return False
    return True


def welcome():
    utils.clear_and_move_cursor()
    print(welcome_text)
    input()


def print_game_status(g: Game):
    print(f'\n目标分数: {g.GOAL}')
    print('附加规则: ')
    print(f'\t{Game.ENABLE_BOAR_BRAWL}\t[{'#' if Game.OPTIONS[Game.ENABLE_BOAR_BRAWL] else ' '}]')
    print(f'\t{Game.ENABLE_SUS_FUSS}\t[{'#' if Game.OPTIONS[Game.ENABLE_SUS_FUSS] else ' '}]')
    print('当前分数: ')
    print(f'\t<{g.player1.name}>: {g.player1.score}(上次 +{g.player1.last_got_score})')
    print(f'\t{g.player1.last_rolls}')
    print(f'\t<{g.player2.name}>: {g.player2.score}(上次 +{g.player2.last_got_score})')
    print(f'\t{g.player2.last_rolls}\n')


if __name__ == '__main__':

    welcome()

    utils.clear_and_move_cursor()
    game = Game(player1_name="路人甲", player2_name="路人乙")

    while True:
        print_game_status(game)
        current_player = game.next_player_round()

        current_input = input(f"<{current_player.name}>, 请掷骰子(0~10): ")

        try:
            number_of_dice = int(current_input)

            if not is_valid_number(number_of_dice):
                raise ValueError

            current_player.shoot_dice(number_of_dice)
            print(current_player.last_rolls)
        except ValueError:
            input(f"无效输入: `{current_input}`, 请重试.")
            current_player = game.next_player_round()  # 防止重新投掷时换到下一个回合
            utils.clear_and_move_cursor()
            continue
        except Exception as e:
            print(e)
            print('其他行为迫使游戏终止')
            break

        need_continue = input('是否继续下一个回合(y/n, 直接回车默认为`y`): ')
        if need_continue == 'y' or need_continue == 'Y' or need_continue == '':
            pass
        elif need_continue == 'n' or need_continue == 'N':
            break

        if game.is_over():
            break

        utils.clear_and_move_cursor()

    utils.clear_and_move_cursor()
    if game.winner == '':
        winner = game.player1.name if game.player1.score > game.player2.score else game.player2.name
        print(f"游戏结束. 获胜者为: {winner}")
    else:
        print(f"游戏结束. 获胜者为: {game.winner}")

    print('比分情况')
    print_game_status(game)
