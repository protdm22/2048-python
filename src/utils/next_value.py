from random import randint


class Next:
    @staticmethod
    def next_value() -> int:
        chance = randint(0, 9)
        if chance == 0:
            return 4
        else:
            return 2
