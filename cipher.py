class Cipher:

    def __init__(self):
        self.action_calls = ("encrypt", "decrypt")

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()



