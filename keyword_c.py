import string

from cipher import Cipher


class KeywordCipher(Cipher):
    PLAIN_TEXT_ALPH = list(string.ascii_uppercase)

    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword
        if not isinstance(keyword, str):
            raise ValueError("You must enter a keyword")
        self.LAST_ALPH = [letter for letter in self.PLAIN_TEXT_ALPH if letter not in self.keyword.upper()]
        self.CIPHER_TEXT_ALPH = list(self.keyword.upper()) + self.LAST_ALPH

    def encrypt(self, message):
        output = []
        for letter in message:
            #  preventing white spaces and numbers
            if letter == ' ' or isinstance(letter, int):
                output.append(letter)
            else:
                idx_in_plain = self.PLAIN_TEXT_ALPH.index(letter.upper())
                output.append(self.CIPHER_TEXT_ALPH[idx_in_plain])
        return "".join(output)

    def decrypt(self, message):
        output = []
        for letter in message:
            #  preventing white spaces and numbers
            if letter == ' ' or isinstance(letter, int):
                output.append(letter)
            else:
                idx_in_plain = self.CIPHER_TEXT_ALPH.index(letter.upper())
                output.append(self.PLAIN_TEXT_ALPH[idx_in_plain])
        return "".join(output)