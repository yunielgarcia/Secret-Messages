import string

from cipher import Cipher


class Bifid(Cipher):
    # for the Polybius square
    NUMB_ROWS = 5
    NUMB_COLUMNS = 5
    PLAIN_TEXT_ALPH = list(string.ascii_uppercase)

    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword
        if not isinstance(keyword, str):
            raise ValueError("You must enter a keyword")
        k_word_upper = self.keyword.upper()

        #  letter shouldn't be repeated in keyword
        seen = {}
        self.clean_keyword = [seen.setdefault(letter, letter) for letter in k_word_upper if letter not in seen]
        # grid
        self.grid = self.construct_grid()

        # In order to fit in the 5x5 grid
        self.alpha = self.PLAIN_TEXT_ALPH[:]
        self.alpha_no_word = [letter for letter in self.alpha if letter not in self.clean_keyword]
        self.alpha_no_word.remove("J")

        # Polybius Square -> dict with format (row, col) : value
        self.polybius_sq = self.fill_square()

    def encrypt(self, message):
        new_coor = self.generate_encryption(message)
        print(new_coor)

    def decrypt(self, message):
        pass

    def construct_grid(self):
        return [(row, col) for row in range(1, (self.NUMB_ROWS + 1)) for col in range(1, (self.NUMB_COLUMNS + 1))]

    def fill_square(self):
        # return the grid populated with the keyword and alphabet with no 'j'
        iter = self.clean_keyword + self.alpha_no_word
        if len(iter) == 25:
            return {(row, col): letter for (row, col), letter in zip(self.grid, iter)}

    def generate_encryption(self, msg):
        """
        Creates two new list one of rows values other of column values
         based in finding of the message's letter in our Polybius Square
        :param msg: Message to encrypt
        """
        msg_up = msg.upper()
        row_list = []
        col_list = []
        for msg_letter in msg_up:
            for (row, col), grid_v in self.polybius_sq.items():
                if msg_letter == grid_v:
                    row_list.append(row)
                    col_list.append(col)

        return self.encryption_coordenates(row_list, col_list)

    def encryption_coordenates(self, row_list, col_list):
        list_added = row_list + col_list
        # return [tuple(list_added[i:i+2]) for i, _ in enumerate(list_added)][::2]
        # return [tuple(list_added[i:i+2]) for i, _ in enumerate(list_added) if not i % 2]
        # return [tuple(list_added[i:i+2]) for i in range(0, len(list_added), 2)]
        return [(list_added[i], list_added[i+1]) for i, _ in enumerate(list_added) if not i % 2]






    # REMEMBER IF THERE IS J IN THE MSG REPLACE IT WITH I
    # IF THE MSG HAS ODD NUM OF LETTER ADD EXTRA LETTER X/Q
