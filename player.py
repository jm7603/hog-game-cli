from typing import Self


class Player(object):

    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.rival: Self = None
        self.last_rolls = []
        self.last_got_score = 0

    def shoot_dice(self, number_of_dice: int):
        from dice import Dice
        current_rolls = [Dice.random_roll() for _ in range(number_of_dice)]
        self.last_rolls = current_rolls
        got_score = Dice.evaluate_score(self, current_rolls)
        self.score += got_score
        self.last_got_score = got_score

    def win(self):
        from game import Game
        return self.score >= Game.GOAL
