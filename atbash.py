import string

from cipher import Cipher


class Atbash(Cipher):
    PLAIN_TEXT_ALPH = list(string.ascii_uppercase)
    REVERSE_TEXT_ALPH = PLAIN_TEXT_ALPH[:]
    REVERSE_TEXT_ALPH.reverse()

    def __init__(self):
        super().__init__()

    def encrypt(self, message):
        """Apply the selected encryption method to the message
        @:param message
        :returns: encrypted message string"""
        encrypted_words = []
        message_up = message.upper()
        for word in message_up.split(" "):
            encrypted_words.append(self.generate_encryption(word))
        return " ".join(encrypted_words)

    def decrypt(self, message):
        decrypted_words = []
        message_up = message.upper()
        for word in message_up.split(" "):
            decrypted_words.append(self.generate_decryption(word))
        return " ".join(decrypted_words)

    def generate_encryption(self, word):
        enc_word = []
        for let in word:
            idx = self.PLAIN_TEXT_ALPH.index(let)
            enc_l = self.REVERSE_TEXT_ALPH[idx]
            enc_word.append(enc_l)
        return "".join(enc_word)

    def generate_decryption(self, word):
        dec_word = []
        for let in word:
            idx = self.REVERSE_TEXT_ALPH.index(let)
            dec_l = self.PLAIN_TEXT_ALPH[idx]
            dec_word.append(dec_l)
        return "".join(dec_word)
