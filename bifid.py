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
        # keyword
        self.clean_keyword = self.clean_prepare_word(self.keyword)
        # grid
        self.grid = self.construct_grid()
        # In order to fit in the 5x5 grid
        self.alpha = self.PLAIN_TEXT_ALPH[:]
        self.alpha_no_word = [letter for letter in self.alpha if letter not in self.clean_keyword]
        try:
            #  It might be already be removed
            self.alpha_no_word.remove("J")
        except ValueError:
            pass

        # Polybius Square (used to encode/decode msg) -> dict with format (row, col) : value
        self.polybius_sq = self.fill_square()

    #   GRID

    def construct_grid(self):
        return [(row, col) for row in range(1, (self.NUMB_ROWS + 1)) for col in range(1, (self.NUMB_COLUMNS + 1))]

    def fill_square(self):
        """return the grid populated with the keyword and alphabet with no 'j'"""
        m_iter = self.clean_keyword + self.alpha_no_word
        if len(m_iter) == 25:
            return {(row, col): letter for (row, col), letter in zip(self.grid, m_iter)}

    def clean_prepare_word(self, key):
        """
        If word come with 'j' remove it then check for even length or fix it
        :return: keyword ready
        """
        k_word_upper = key.upper()

        #  letter shouldn't be repeated in keyword
        seen = {}
        clean_keyword = [seen.setdefault(letter, letter) for letter in k_word_upper if letter not in seen]
        try:
            clean_keyword.remove("J")
        except ValueError:
            pass

        return clean_keyword

    #  ENCRYPTION

    def encrypt(self, message):
        """
        Encrypt the message
        :param message:
        :return: Message encrypted
        """
        encrypted_words = []
        #  The length of the msg must be even.
        #  we add any unusual letter that doesn't affect the msg understanding
        if not len(message) % 2 == 0:
            message += "x"
        for word in message.split(" "):
            encrypted_words.append(self.generate_encryption(word))
        return " ".join(encrypted_words)

    def generate_encryption(self, word):
        """
        Creates two new list one of rows values other of column values
         based in finding of the message's letter in our Polybius Square
        :param word: Message to encrypt
        """
        msg_up = word.upper()
        row_list = []
        col_list = []
        for msg_letter in msg_up:
            for (row, col), grid_v in self.polybius_sq.items():
                if msg_letter == "J":
                    msg_letter = "I"
                if msg_letter == grid_v:
                    row_list.append(row)
                    col_list.append(col)

        return self.encryption_coordinates(row_list, col_list)

    def encryption_coordinates(self, row_list, col_list):
        list_added = row_list + col_list
        # [tuple(list_added[i:i+2]) for i, _ in enumerate(list_added)][::2]
        # [tuple(list_added[i:i+2]) for i, _ in enumerate(list_added) if not i % 2]
        # [tuple(list_added[i:i+2]) for i in range(0, len(list_added), 2)]
        new_word_coordinates = [(list_added[i], list_added[i + 1]) for i, _ in enumerate(list_added) if not i % 2]
        return self.word_for_coordinates(new_word_coordinates)

    #  Used by both methods enc/dec
    def word_for_coordinates(self, word_coord):
        """
        encrypt the single word passed, using its encrypted coordinates
        :param word_coord:
        :return: word encrypted
        """
        word = []
        for coord in word_coord:
            word.append(self.polybius_sq[coord])
        return "".join(word)

    #  DECRYPTION

    def decrypt(self, message):
        decrypted_words = []
        #  The length of the msg must be even.
        #  we add any unusual letter that doesn't affect the msg understanding
        if not len(message) % 2 == 0:
            message += "x"
        for word in message.split(" "):
            decrypted_words.append(self.generate_decryption(word))
        return " ".join(decrypted_words)

    def generate_decryption(self, word_enc):
        coord_for_decrypt = []
        for letter_enc in word_enc:
            for (row, col), grid_v in self.polybius_sq.items():
                if letter_enc == grid_v:
                    coord_for_decrypt.extend([row, col])
        return self.decrypt_word(coord_for_decrypt)

    def decrypt_word(self, coord_for_decrypt):
        """
            decrypt the single word passed, using its decrypted coordinates
            :param coord_for_decrypt:
            :return: word decrypted
        """
        word = []
        half = int(len(coord_for_decrypt) / 2)  # We are sure is even. Checking that in first method
        # print([(row, col) for row, col in zip(coord_for_decrypt[:half], coord_for_decrypt[half:])])
        coordinates = [(row, col) for row, col in zip(coord_for_decrypt[:half], coord_for_decrypt[half:])]
        return self.word_for_coordinates(coordinates)
