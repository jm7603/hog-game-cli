import random

import utils
from game import Game
from player import Player


class Dice(object):

    @staticmethod
    def random_roll() -> int:
        return random.randint(1, 6)

    @staticmethod
    def evaluate_score(player: Player, current_rolls: list) -> int:
        sum_of_rolls = sum(current_rolls)
        this_final_score = 0
        if Game.OPTIONS[Game.ENABLE_BOAR_BRAWL] and sum_of_rolls == 0:
            input('触发事件: 野猪乱斗')
            ten_place_of_rival_score = player.rival.score // 10 % 10
            one_place_of_self_score = player.score % 10
            res = 3 * abs(ten_place_of_rival_score - one_place_of_self_score)
            this_final_score += res if res != 0 else 1

        if 1 in current_rolls:
            input('触发事件: 母猪哭泣')
            this_final_score += 1
        else:
            this_final_score += sum_of_rolls

        if Game.OPTIONS[Game.ENABLE_SUS_FUSS]:
            after_score = player.score + this_final_score
            if utils.factor_count(after_score) in [3, 4]:
                input('触发事件: 疑神疑鬼')
                this_final_score = utils.next_prime(after_score)

        return this_final_score
