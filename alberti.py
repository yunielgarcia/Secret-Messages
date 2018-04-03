from random import shuffle
import string

from cipher import Cipher


class Alberti(Cipher):

    def __init__(self):
        self.INNER_DISC_RANDOM = self._init_inner_disc_random()
        print(self.INNER_DISC_RANDOM)

    @staticmethod
    def _init_inner_disc_random():
        inner_up_r = list(string.ascii_uppercase)
        shuffle(inner_up_r)
        return inner_up_r
